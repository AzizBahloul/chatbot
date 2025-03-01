import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

MODEL_PATH = "transformer_chatbot"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = TFAutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

def chat_with_bot(user_input):
    input_text = "chatbot: " + user_input
    inputs = tokenizer(input_text, return_tensors="tf", padding="max_length", truncation=True, max_length=128)
    outputs = model.generate(inputs.input_ids, max_length=128, num_beams=5, early_stopping=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

print("Chat with the bot (type 'exit' to stop):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chat_with_bot(user_input))
