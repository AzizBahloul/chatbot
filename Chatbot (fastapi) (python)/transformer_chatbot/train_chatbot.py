import os
import argparse
import numpy as np
import tensorflow as tf
from datasets import load_dataset
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer, TFTrainer, TFTrainingArguments
from huggingface_hub import login
from dotenv import load_dotenv

def parse_args():
    parser = argparse.ArgumentParser(description="Train a chatbot using a transformer model")
    parser.add_argument("--model_name", type=str, default="t5-small", help="Model name from HuggingFace")
    parser.add_argument("--dataset_name", type=str, default="lmsys/chat-1m", help="Dataset name from HuggingFace")
    parser.add_argument("--dataset_split", type=str, default="train[:5%]", help="Dataset split to use")
    parser.add_argument("--batch_size", type=int, default=8, help="Training batch size")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--max_length", type=int, default=128, help="Max sequence length")
    parser.add_argument("--learning_rate", type=float, default=3e-5, help="Learning rate")
    parser.add_argument("--save_path", type=str, default="transformer_chatbot", help="Path to save the model")
    parser.add_argument("--use_mixed_precision", action="store_true", help="Use mixed precision training")
    parser.add_argument("--validation_split", type=float, default=0.1, help="Validation data percentage")
    return parser.parse_args()

def preprocess_function(examples, tokenizer, max_length):
    """Tokenize inputs and labels for training."""
    # Extract input and output texts
    input_texts = ["chatbot: " + ex for ex in examples['text']] 
    labels = examples['response']
    
    # Tokenize inputs and labels
    inputs = tokenizer(input_texts, max_length=max_length, padding="max_length", truncation=True, return_tensors="tf")
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(labels, max_length=max_length, padding="max_length", truncation=True, return_tensors="tf").input_ids
    
    # Replace padding token id's with -100 to ignore in loss calculation
    labels = np.array(labels)
    labels[labels == tokenizer.pad_token_id] = -100
    
    return {"input_ids": inputs.input_ids, "attention_mask": inputs.attention_mask, "labels": labels}

def main():
    # Load environment variables for secrets
    load_dotenv()
    
    # Parse arguments
    args = parse_args()
    
    # Enable mixed precision if requested
    if args.use_mixed_precision:
        policy = tf.keras.mixed_precision.Policy('mixed_float16')
        tf.keras.mixed_precision.set_global_policy(policy)
        print("Using mixed precision training")
    
    # Authenticate with Hugging Face
    try:
        hf_token = os.environ.get("HF_API_TOKEN")
        if not hf_token:
            print("Warning: HF_API_TOKEN not found in environment variables")
        else:
            login(hf_token)
    except Exception as e:
        print(f"Authentication error: {e}")
        print("Continuing without authentication...")
    
    # Load dataset
    print(f"Loading dataset {args.dataset_name}...")
    try:
        dataset = load_dataset(args.dataset_name, split=args.dataset_split)
        
        # Split into train and validation sets
        dataset = dataset.train_test_split(test_size=args.validation_split)
        train_dataset = dataset['train']
        validation_dataset = dataset['test']
        
        print(f"Train dataset size: {len(train_dataset)}")
        print(f"Validation dataset size: {len(validation_dataset)}")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
    
    # Load tokenizer and model
    print(f"Loading model {args.model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = TFAutoModelForSeq2SeqLM.from_pretrained(args.model_name)
    
    # Add preprocessing function with fixed parameters
    preprocess = lambda examples: preprocess_function(examples, tokenizer, args.max_length)
    
    # Prepare datasets for training
    print("Processing datasets...")
    processed_train = train_dataset.map(preprocess, batched=True)
    processed_val = validation_dataset.map(preprocess, batched=True)
    
    processed_train.set_format(type='tensorflow', columns=['input_ids', 'attention_mask', 'labels'])
    processed_val.set_format(type='tensorflow', columns=['input_ids', 'attention_mask', 'labels'])
    
    # Convert to TensorFlow datasets
    tf_train_dataset = processed_train.to_tf_dataset(
        columns=['input_ids', 'attention_mask'],
        label_cols=['labels'],
        shuffle=True,
        batch_size=args.batch_size
    )
    
    tf_val_dataset = processed_val.to_tf_dataset(
        columns=['input_ids', 'attention_mask'],
        label_cols=['labels'],
        shuffle=False,
        batch_size=args.batch_size
    )
    
    # Setup optimizer with learning rate schedule
    steps_per_epoch = len(processed_train) // args.batch_size
    total_steps = steps_per_epoch * args.epochs
    
    lr_schedule = tf.keras.optimizers.schedules.PolynomialDecay(
        initial_learning_rate=args.learning_rate,
        decay_steps=total_steps,
        end_learning_rate=args.learning_rate / 10.0,
    )
    
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
    
    # Setup callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True),
        tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(args.save_path, "checkpoints/model_{epoch}"),
            save_best_only=True,
            monitor='val_loss'
        ),
        tf.keras.callbacks.TensorBoard(log_dir=os.path.join(args.save_path, "logs"))
    ]
    
    # Compile model
    model.compile(optimizer=optimizer, loss=model.compute_loss)
    
    # Train model
    print("Training model...")
    model.fit(
        tf_train_dataset,
        validation_data=tf_val_dataset,
        epochs=args.epochs,
        callbacks=callbacks
    )
    
    # Save model and tokenizer
    final_save_path = os.path.join(args.save_path, "final_model")
    os.makedirs(final_save_path, exist_ok=True)
    print(f"Saving model to {final_save_path}...")
    model.save_pretrained(final_save_path)
    tokenizer.save_pretrained(final_save_path)
    print(f"Model saved successfully")

if __name__ == "__main__":
    main()
