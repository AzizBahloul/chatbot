import pandas as pd
import random

# Previous 100 question-response pairs (in English)
qa_pairs = [
    ("Hello", "Hi there!"),
    ("How are you?", "I'm doing well, thank you for asking. How about you?"),
    ("What's your name?", "My name is ChatBot. Nice to meet you!"),
    ("What do you do?", "I'm an AI assistant designed to help answer questions and provide information."),
    ("How old are you?", "As an AI, I don't have an age in the traditional sense. I was recently created."),
    ("Where are you from?", "I'm a digital creation, so I don't have a physical place of origin."),
    ("What's the weather like?", "I'm sorry, I don't have access to real-time weather information. You might want to check a weather app or website for that."),
    ("Tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
    ("What's the meaning of life?", "That's a profound question! Philosophers have debated this for centuries. What do you think?"),
    ("Can you help me?", "I'd be happy to try! What do you need assistance with?"),
    ("What time is it?", "I'm sorry, I don't have access to real-time clock information. You can check your device for the current time."),
    ("Do you sleep?", "As an AI, I don't sleep. I'm always available to help!"),
    ("What's your favorite color?", "As an AI, I don't have personal preferences, but I find all colors fascinating!"),
    ("Are you human?", "No, I'm an AI language model. I'm here to assist and chat, but I'm not human."),
    ("What languages do you speak?", "I'm trained to understand and communicate in many languages, but we're chatting in English right now."),
    ("Tell me about yourself", "I'm an AI assistant created to help with various tasks and answer questions. What would you like to know?"),
    ("Do you have feelings?", "As an AI, I don't have feelings or emotions in the way humans do. I'm designed to assist and provide information."),
    ("What's the capital of France?", "The capital of France is Paris."),
    ("How do I make pasta?", "To make pasta, boil water, add salt, cook the pasta according to package instructions, then drain and serve with your favorite sauce."),
    ("What's the largest planet in our solar system?", "Jupiter is the largest planet in our solar system."),
    ("How far is the moon from Earth?", "The average distance between the Earth and the moon is about 238,855 miles (384,400 km)."),
    ("Who wrote Romeo and Juliet?", "Romeo and Juliet was written by William Shakespeare."),
    ("What's the boiling point of water?", "Water boils at 100°C (212°F) at sea level."),
    ("How many continents are there?", "There are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia (Oceania), and South America."),
    ("What's the fastest land animal?", "The cheetah is the fastest land animal, capable of running up to 70 mph (112 km/h)."),
    ("Who painted the Mona Lisa?", "The Mona Lisa was painted by Leonardo da Vinci."),
    ("What's the largest ocean?", "The Pacific Ocean is the largest and deepest ocean on Earth."),
    ("How many bones are in the human body?", "An adult human body has 206 bones."),
    ("What's the chemical symbol for gold?", "The chemical symbol for gold is Au."),
    ("Who invented the telephone?", "Alexander Graham Bell is credited with inventing the telephone."),
    ("What's the tallest mountain in the world?", "Mount Everest is the tallest mountain above sea level, at 29,029 feet (8,848 meters)."),
    ("How many planets are in our solar system?", "There are eight planets in our solar system since Pluto was reclassified as a dwarf planet."),
    ("What's the capital of Japan?", "The capital of Japan is Tokyo."),
    ("Who wrote 'To Kill a Mockingbird'?", "To Kill a Mockingbird was written by Harper Lee."),
    ("What's the largest mammal?", "The blue whale is the largest mammal, and the largest animal to have ever existed on Earth."),
    ("How many sides does a triangle have?", "A triangle has three sides."),
    ("What's the main ingredient in guacamole?", "The main ingredient in guacamole is avocado."),
    ("Who was the first person to walk on the moon?", "Neil Armstrong was the first person to walk on the moon."),
    ("What's the fastest bird?", "The peregrine falcon is the fastest bird, and the fastest member of the animal kingdom."),
    ("How many teeth does an adult human have?", "An adult human typically has 32 teeth."),
    ("What's the largest country by land area?", "Russia is the largest country by land area."),
    ("Who painted 'Starry Night'?", "Starry Night was painted by Vincent van Gogh."),
    ("What's the smallest planet in our solar system?", "Mercury is the smallest planet in our solar system."),
    ("How many hearts does an octopus have?", "An octopus has three hearts."),
    ("What's the main language spoken in Brazil?", "The main language spoken in Brazil is Portuguese."),
    ("Who wrote '1984'?", "1984 was written by George Orwell."),
    ("What's the chemical formula for water?", "The chemical formula for water is H2O."),
    ("How many strings does a violin have?", "A violin typically has four strings."),
    ("What's the largest desert in the world?", "The largest desert in the world is the Antarctic Desert, followed by the Sahara Desert."),
    ("Who discovered penicillin?", "Penicillin was discovered by Alexander Fleming."),
    ("What's the longest river in the world?", "The Nile is generally considered the longest river in the world."),
    ("How many time zones are there in Russia?", "Russia spans 11 time zones."),
    ("What's the smallest bone in the human body?", "The smallest bone in the human body is the stapes, located in the middle ear."),
    ("Who composed the 'Moonlight Sonata'?", "The 'Moonlight Sonata' was composed by Ludwig van Beethoven."),
    ("What's the largest species of bear?", "The largest species of bear is the polar bear."),
    ("How many keys are on a standard piano?", "A standard piano has 88 keys."),
    ("What's the capital of Australia?", "The capital of Australia is Canberra."),
    ("Who wrote 'The Great Gatsby'?", "The Great Gatsby was written by F. Scott Fitzgerald."),
    ("What's the deepest point in the ocean?", "The deepest point in the ocean is the Challenger Deep in the Mariana Trench."),
    ("How many players are on a soccer team?", "A soccer team has 11 players on the field."),
    ("What's the most abundant gas in Earth's atmosphere?", "The most abundant gas in Earth's atmosphere is nitrogen."),
    ("Who painted the Sistine Chapel ceiling?", "The Sistine Chapel ceiling was painted by Michelangelo."),
    ("What's the largest organ in the human body?", "The largest organ in the human body is the skin."),
    ("How many faces does a cube have?", "A cube has six faces."),
    ("What's the capital of Canada?", "The capital of Canada is Ottawa."),
    ("Who wrote 'Pride and Prejudice'?", "Pride and Prejudice was written by Jane Austen."),
    ("What's the smallest country in the world?", "The smallest country in the world is Vatican City."),
    ("How many chromosomes do humans have?", "Humans have 23 pairs of chromosomes, for a total of 46."),
    ("What's the largest bird in the world?", "The largest bird in the world is the ostrich."),
    ("Who invented the light bulb?", "Thomas Edison is credited with inventing the first commercially successful incandescent light bulb."),
    ("What's the longest word in the English language?", "The longest word in English is the chemical name for titin, with 189,819 letters."),
    ("How many elements are in the periodic table?", "There are currently 118 elements in the periodic table."),
    ("What's the capital of Spain?", "The capital of Spain is Madrid."),
    ("Who wrote 'Hamlet'?", "Hamlet was written by William Shakespeare."),
    ("What's the largest island in the world?", "Greenland is the largest island in the world."),
    ("How many legs does a spider have?", "A spider has eight legs."),
    ("What's the main ingredient in hummus?", "The main ingredient in hummus is chickpeas."),
    ("Who painted 'The Persistence of Memory'?", "The Persistence of Memory was painted by Salvador Dalí."),
    ("What's the hardest natural substance on Earth?", "The hardest natural substance on Earth is diamond."),
    ("How many sides does a hexagon have?", "A hexagon has six sides."),
    ("What's the capital of Egypt?", "The capital of Egypt is Cairo."),
    ("Who wrote 'War and Peace'?", "War and Peace was written by Leo Tolstoy."),
    ("What's the largest type of big cat?", "The largest type of big cat is the tiger."),
    ("How many teeth does an adult dog have?", "An adult dog typically has 42 teeth."),
    ("What's the main language spoken in Argentina?", "The main language spoken in Argentina is Spanish."),
    ("Who discovered gravity?", "Sir Isaac Newton is credited with discovering gravity."),
    ("What's the smallest ocean?", "The smallest ocean is the Arctic Ocean."),
    ("How many stars are on the American flag?", "The American flag has 50 stars."),
    ("What's the capital of Italy?", "The capital of Italy is Rome."),
    ("Who wrote 'The Odyssey'?", "The Odyssey is attributed to the ancient Greek poet Homer."),
    ("What's the largest flying bird?", "The largest flying bird by wingspan is the wandering albatross."),
    ("How many continents are there?", "There are seven continents."),
    ("What's the main ingredient in sushi?", "The main ingredient in sushi is vinegared rice."),
    ("Who invented the telephone?", "Alexander Graham Bell is credited with inventing the telephone."),
    ("What's the largest asteroid in the asteroid belt?", "The largest asteroid in the asteroid belt is Ceres."),
    ("How many moons does Mars have?", "Mars has two moons: Phobos and Deimos."),
    ("What's the capital of China?", "The capital of China is Beijing."),
    ("Who wrote 'The Catcher in the Rye'?", "The Catcher in the Rye was written by J.D. Salinger."),
    ("What's the largest species of shark?", "The largest species of shark is the whale shark."),
    ("How many bones are in the human hand?", "There are 27 bones in the human hand."),
    ("What's the main language spoken in Germany?", "The main language spoken in Germany is German.")
]
# Previous 100 question-response pairs in Tunisian Derja
tunisian_qa_pairs = [
    ("Aslema", "Aslema, kifech enti?"),
    ("Chneya 7welek?", "Hamdullah, labess. W enti?"),
    ("Chesmek?", "Esmi ChatBot. Tcharrafna"),
    ("Chnouwa ta3mel?", "Ana robot dhaki, njem n3awen fi barcha 7ajet"),
    ("9addech 3andek?", "Ma3andich 3mer m7added. Ana programme informatique"),
    ("Mnin enti?", "Ana mawjoud 3al internet, ma3andich blasa fizikiya"),
    ("Chnouwa jaw lyoum?", "Ana ma3andich ma3loumet 3al jaw. Chouf application ta9s"),
    ("9olli nokta", "Chbih el 7out ki yechreb 9ahwa? Yewalli dauphin"),
    ("Chneya ma3na el 7ayet?", "Hadha soueel 3ami9. Kol wa7ed 3andou ijebetou el khassa"),
    ("Tnajem t3aweni?", "Inchallah, chnouwa el mochkla?"),
    ("9addech tawa?", "Ma3andich sa3a, ama tnajem tchouf fi telephonek"),
    ("Tor9od?", "La, ana programme, ma nor9odch"),
    ("Chneya lonk el mfaddal 3andek?", "Ana ma3andich tafdhilet. El alwen elkoll behyin"),
    ("Enti insen?", "La, ana intelligence artificielle, mich insen"),
    ("Chkoun languages taaref?", "Na7ki barcha loghat, ama tawa na7kiw bil derja"),
    ("A7kili 3ala rou7ek", "Ana programme dhaki, mawjoud bech n3awen w njeweb 3ala as2ila"),
    ("3andek mche3er?", "La, ana ma3andich mche3er. Ana programme informatique"),
    ("Chneya 3asmet fransa?", "3asmet fransa hiya Paris"),
    ("Kifech na3mel pasta?", "Tfowwer el me, tzid mel7, w ba3d t7ot el pasta w tkhaliha tatayeb"),
    ("Chneya akbar kawkab fil majmou3a echamsia?", "Akbar kawkab fil majmou3a echamsia howa Jupiter"),
    ("9addech ba3id el 9amar 3al ardh?", "El 9amar yeb3ed 3al ardh 384,400 km t9riban"),
    ("Chkoun kteb Romeo w Juliet?", "Elli kteb Romeo w Juliet howa William Shakespeare"),
    ("3la 9addech el me yaghli?", "El me yaghli 3la 100 darajat"),
    ("9addech min 9arra mawjoudin?", "Mawjoudin 7 9arrat fil 3alem"),
    ("Chneya as-ra3 7ayawen?", "El fahd (cheetah) howa as-ra3 7ayawen barri"),
    ("Chkoun rasem el Mona Lisa?", "Elli rasem el Mona Lisa howa Leonardo da Vinci"),
    ("Chneya akbar m7it?", "Akbar m7it howa el m7it el hedi"),
    ("9addech min 3adhem fil jism el inseni?", "Fil jism el inseni mawjoud 206 3adhem"),
    ("Chneya ermez el kimye2i mta3 edhahab?", "Ermez el kimye2i mta3 edhahab howa Au"),
    ("Chkoun khtara3 el telephone?", "Elli khtara3 el telephone howa Alexander Graham Bell"),
    ("Chneya a3la jbel fil 3alem?", "A3la jbel fil 3alem howa Mount Everest"),
    ("9addech min kawkab fil majmou3a echamsia?", "Fil majmou3a echamsia mawjoudin 8 kawekeb"),
    ("Chneya 3asmet el yaben?", "3asmet el yaben hiya Tokyo"),
    ("Chkoun kteb 'To Kill a Mockingbird'?", "'To Kill a Mockingbird' ktebha Harper Lee"),
    ("Chneya akbar 7ayawen labboun?", "Akbar 7ayawen labboun howa el 7out el azra9"),
    ("9addech min dhala3 3and el mthalleth?", "El mthalleth 3andou 3 dhoulou3"),
    ("Chneya el ingredient el asesi fil guacamole?", "El ingredient el asesi fil guacamole howa el avocado"),
    ("Chkoun awel wa7ed mcha 3al 9amar?", "Awel wa7ed mcha 3al 9amar howa Neil Armstrong"),
    ("Chneya as-ra3 3asfour?", "As-ra3 3asfour howa el chahine"),
    ("9addech min sinna 3and el insen el kebir?", "El insen el kebir 3andou 32 sinna"),
    ("Chneya akbar bled mil mse7a?", "Akbar bled mil mse7a hiya Russia"),
    ("Chkoun rasem 'Starry Night'?", "'Starry Night' rasmha Vincent van Gogh"),
    ("Chneya as-ghar kawkab fil majmou3a echamsia?", "As-ghar kawkab fil majmou3a echamsia howa Mercury"),
    ("9addech min 9alb 3and el akhtabout?", "El akhtabout 3andou 3 9loub"),
    ("Chneya el logha el asesiya fil Brazil?", "El logha el asesiya fil Brazil hiya el Portugali"),
    ("Chkoun kteb '1984'?", "'1984' ktebha George Orwell"),
    ("Chneya es-sigha el kimye2iya lil me?", "Es-sigha el kimye2iya lil me hiya H2O"),
    ("9addech min watar 3and el kemenja?", "El kemenja 3andha 4 awtar"),
    ("Chneya akbar sa7ra fil 3alem?", "Akbar sa7ra fil 3alem hiya sa7ret el Antarctica, w ba3dha es-sa7ra el kubra"),
    ("Chkoun ktechef el peniciline?", "Elli ktechef el peniciline howa Alexander Fleming"),
    ("Chneya atwal nhar fil 3alem?", "Atwal nhar fil 3alem howa nhar el Nil"),
    ("9addech min zone de temps fi Russia?", "Fi Russia mawjoudin 11 zones de temps"),
    ("Chneya as-ghar 3adhem fil jism el inseni?", "As-ghar 3adhem fil jism el inseni howa el 3adhem el rekabi fil wedhnin"),
    ("Chkoun allef 'Moonlight Sonata'?", "'Moonlight Sonata' allefha Ludwig van Beethoven"),
    ("Chneya akbar naw3 mta3 ed-dob?", "Akbar naw3 mta3 ed-dob howa ed-dob el 9otbi"),
    ("9addech min touche 3and el piano el 3adi?", "El piano el 3adi 3andou 88 touche"),
    ("Chneya 3asmet Australia?", "3asmet Australia hiya Canberra"),
    ("Chkoun kteb 'The Great Gatsby'?", "'The Great Gatsby' ktebha F. Scott Fitzgerald"),
    ("Win mawjoud a3ma9 no9ta fil ba7r?", "A3ma9 no9ta fil ba7r mawjouda fil Challenger Deep fil Mariana Trench"),
    ("9addech min la3eb fil fari9 mta3 el koura?", "Fari9 el koura fih 11 la3eb"),
    ("Chneya akther ghez mawjoud fil jaw?", "Akther ghez mawjoud fil jaw howa el azote"),
    ("Chkoun rasem s9af el Chapelle Sixtine?", "Elli rasem s9af el Chapelle Sixtine howa Michelangelo"),
    ("Chneya akbar 3odw fil jism el inseni?", "Akbar 3odw fil jism el inseni howa el jild"),
    ("9addech min wajh 3and el moka33ab?", "El moka33ab 3andou 6 wjouh"),
    ("Chneya 3asmet Canada?", "3asmet Canada hiya Ottawa"),
    ("Chkoun kteb 'Pride and Prejudice'?", "'Pride and Prejudice' ktebha Jane Austen"),
    ("Chneya as-ghar dawla fil 3alem?", "As-ghar dawla fil 3alem hiya el Vatican"),
    ("9addech min chromosome 3and el insen?", "El insen 3andou 23 zawj mta3 chromosomes, ya3ni 46 fil majmou3"),
    ("Chneya akbar 3asfour fil 3alem?", "Akbar 3asfour fil 3alem howa enna3ema"),
    ("Chkoun khtara3 el lampe?", "Elli khtara3 el lampe el kahrabiya howa Thomas Edison"),
    ("Chneya atwal kelma fil logha el angliziya?", "Atwal kelma fil logha el angliziya hiya esm kimye2i fih 189,819 7arf"),
    ("9addech min 3onsor fil jadwal el dawri?", "Fil jadwal el dawri mawjoudin 118 3onsor"),
    ("Chneya 3asmet Espania?", "3asmet Espania hiya Madrid"),
    ("Chkoun kteb 'Hamlet'?", "'Hamlet' ktebha William Shakespeare"),
    ("Chneya akbar jazira fil 3alem?", "Akbar jazira fil 3alem hiya Greenland"),
    ("9addech min rejl 3and el 3ankabout?", "El 3ankabout 3andou 8 rejlin"),
    ("Chneya el ingredient el asesi fil hommos?", "El ingredient el asesi fil hommos howa el 7ommos"),
    ("Chkoun rasem 'The Persistence of Memory'?", "'The Persistence of Memory' rasmha Salvador Dalí"),
    ("Chneya aqwa madda fil tabi3a?", "Aqwa madda fil tabi3a howa el mass"),
    ("9addech min dhala3 3and el mosaddas?", "El mosaddas 3andou 6 dhoulou3"),
    ("Chneya 3asmet Masr?", "3asmet Masr hiya El Qahira"),
    ("Chkoun kteb 'El 7arb w Es-silm'?", "'El 7arb w Es-silm' (War and Peace) ktebha Leo Tolstoy"),
    ("Chneya akbar naw3 mta3 el 9tot el kbira?", "Akbar naw3 mta3 el 9tot el kbira howa ennemr"),
    ("9addech min sinna 3and el kelb el kebir?", "El kelb el kebir 3andou 42 sinna"),
    ("Chneya el logha el asesiya fil Argentina?", "El logha el asesiya fil Argentina hiya el Espaniol"),
    ("Chkoun ktechef el jedhbiya?", "Elli ktechef el jedhbiya howa Sir Isaac Newton"),
    ("Chneya as-ghar m7it?", "As-ghar m7it howa el m7it el motajammid ech-chemali"),
    ("9addech min najma fil 3alam el amerikani?", "El 3alam el amerikani fih 50 najma"),
    ("Chneya 3asmet Italia?", "3asmet Italia hiya Roma"),
    ("Chkoun kteb 'El Odyssée'?", "'El Odyssée' ktebha Homer"),
    ("Chneya akbar 3asfour ytir?", "Akbar 3asfour ytir (mil jne7) howa el albatros"),
    ("9addech min 9arra fil 3alem?", "Fil 3alem mawjoudin 7 9arrat"),
    ("Chneya el ingredient el asesi fil sushi?", "El ingredient el asesi fil sushi howa el rouz bil khall"),
    ("Chkoun khtara3 el telephone?", "Elli khtara3 el telephone howa Alexander Graham Bell"),
    ("Chneya akbar asteroid fil 7zem mta3 el asteroids?", "Akbar asteroid fil 7zem mta3 el asteroids howa Ceres"),
    ("9addech min 9amar 3and el kawkab Mars?", "El kawkab Mars 3andou zouz 9marat: Phobos w Deimos"),
    ("Chneya 3asmet Es-Sin?", "3asmet Es-Sin hiya Beijing"),
    ("Chkoun kteb 'El 7aris fil 7a9l mta3 el choufan'?", "'El 7aris fil 7a9l mta3 el choufan' (The Catcher in the Rye) ktebha J.D. Salinger"),
    ("Chneya akbar naw3 mta3 el 9arch?", "Akbar naw3 mta3 el 9arch howa 9arch el 7out"),
    ("9addech min 3adhem fil yedd mta3 el insen?", "Fil yedd mta3 el insen mawjoudin 27 3adhem"),
    ("Chneya el logha el asesiya fil Almenia?", "El logha el asesiya fil Almenia hiya el Almeni")
]

# Additional 100 question-response pairs in French
french_qa_pairs = [
    ("Bonjour", "Bonjour ! Comment allez-vous ?"),
    ("Comment allez-vous ?", "Je vais bien, merci. Et vous ?"),
    ("Comment vous appelez-vous ?", "Je m'appelle ChatBot. Ravi de vous rencontrer !"),
    ("Que faites-vous ?", "Je suis un assistant virtuel conçu pour répondre à vos questions et vous aider."),
    ("Quel âge avez-vous ?", "Je n'ai pas d'âge défini. Je suis un programme informatique récemment créé."),
    ("D'où venez-vous ?", "Je suis une création numérique, je n'ai pas d'origine physique."),
    ("Quel temps fait-il aujourd'hui ?", "Désolé, je n'ai pas accès aux informations météorologiques en temps réel."),
    ("Racontez-moi une blague", "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau !"),
    ("Quel est le sens de la vie ?", "C'est une question profonde ! Les philosophes en débattent depuis des siècles. Qu'en pensez-vous ?"),
    ("Pouvez-vous m'aider ?", "Bien sûr, je serai ravi d'essayer. Quelle est votre question ?"),
    ("Quelle heure est-il ?", "Je n'ai pas d'horloge intégrée. Vous pouvez vérifier l'heure sur votre appareil."),
    ("Dormez-vous ?", "Non, je suis un programme informatique. Je suis toujours disponible."),
    ("Quelle est votre couleur préférée ?", "En tant qu'IA, je n'ai pas de préférences personnelles. Toutes les couleurs sont fascinantes !"),
    ("Êtes-vous humain ?", "Non, je suis une intelligence artificielle. Je suis là pour discuter et aider, mais je ne suis pas humain."),
    ("Quelles langues parlez-vous ?", "Je suis programmé pour comprendre et communiquer dans de nombreuses langues. Nous parlons français en ce moment."),
    ("Parlez-moi de vous", "Je suis une IA créée pour aider avec diverses tâches et répondre à des questions. Que voulez-vous savoir ?"),
    ("Avez-vous des sentiments ?", "En tant qu'IA, je n'ai pas de sentiments ou d'émotions comme les humains. Je suis conçu pour assister et fournir des informations."),
    ("Quelle est la capitale de la France ?", "La capitale de la France est Paris."),
    ("Comment faire des pâtes ?", "Pour faire des pâtes, faites bouillir de l'eau, ajoutez du sel, cuisez les pâtes selon les instructions du paquet, puis égouttez-les et servez avec votre sauce préférée."),
    ("Quelle est la plus grande planète du système solaire ?", "Jupiter est la plus grande planète de notre système solaire."),
    ("À quelle distance est la Lune de la Terre ?", "La distance moyenne entre la Terre et la Lune est d'environ 384 400 km."),
    ("Qui a écrit 'Roméo et Juliette' ?", "Roméo et Juliette a été écrit par William Shakespeare."),
    ("Quelle est la température d'ébullition de l'eau ?", "L'eau bout à 100°C (212°F) au niveau de la mer."),
    ("Combien y a-t-il de continents ?", "Il y a sept continents : Afrique, Antarctique, Asie, Europe, Amérique du Nord, Océanie et Amérique du Sud."),
    ("Quel est l'animal terrestre le plus rapide ?", "Le guépard est l'animal terrestre le plus rapide, capable de courir jusqu'à 112 km/h."),
    ("Qui a peint la Joconde ?", "La Joconde a été peinte par Léonard de Vinci."),
    ("Quel est le plus grand océan ?", "L'océan Pacifique est le plus grand et le plus profond océan de la Terre."),
    ("Combien d'os y a-t-il dans le corps humain ?", "Un corps humain adulte compte 206 os."),
    ("Quel est le symbole chimique de l'or ?", "Le symbole chimique de l'or est Au."),
    ("Qui a inventé le téléphone ?", "Alexander Graham Bell est crédité de l'invention du téléphone."),
    ("Quelle est la plus haute montagne du monde ?", "Le mont Everest est la plus haute montagne au-dessus du niveau de la mer, à 8 848 mètres."),
    ("Combien y a-t-il de planètes dans notre système solaire ?", "Il y a huit planètes dans notre système solaire depuis que Pluton a été reclassé comme planète naine."),
    ("Quelle est la capitale du Japon ?", "La capitale du Japon est Tokyo."),
    ("Qui a écrit 'Ne tirez pas sur l'oiseau moqueur' ?", "Ne tirez pas sur l'oiseau moqueur a été écrit par Harper Lee."),
    ("Quel est le plus grand mammifère ?", "La baleine bleue est le plus grand mammifère, et le plus grand animal ayant jamais existé sur Terre."),
    ("Combien de côtés a un triangle ?", "Un triangle a trois côtés."),
    ("Quel est l'ingrédient principal du guacamole ?", "L'ingrédient principal du guacamole est l'avocat."),
    ("Qui a été le premier homme à marcher sur la Lune ?", "Neil Armstrong a été le premier homme à marcher sur la Lune."),
    ("Quel est l'oiseau le plus rapide ?", "Le faucon pèlerin est l'oiseau le plus rapide, et le membre le plus rapide du règne animal."),
    ("Combien de dents un adulte humain a-t-il ?", "Un adulte humain a généralement 32 dents."),
    ("Quel est le plus grand pays par superficie ?", "La Russie est le plus grand pays par superficie."),
    ("Qui a peint 'La Nuit étoilée' ?", "La Nuit étoilée a été peinte par Vincent van Gogh."),
    ("Quelle est la plus petite planète du système solaire ?", "Mercure est la plus petite planète de notre système solaire."),
    ("Combien de cœurs a une pieuvre ?", "Une pieuvre a trois cœurs."),
    ("Quelle est la langue principale parlée au Brésil ?", "La langue principale parlée au Brésil est le portugais."),
    ("Qui a écrit '1984' ?", "1984 a été écrit par George Orwell."),
    ("Quelle est la formule chimique de l'eau ?", "La formule chimique de l'eau est H2O."),
    ("Combien de cordes a un violon ?", "Un violon a généralement quatre cordes."),
    ("Quel est le plus grand désert du monde ?", "Le plus grand désert du monde est le désert de l'Antarctique, suivi du Sahara."),
    ("Qui a découvert la pénicilline ?", "La pénicilline a été découverte par Alexander Fleming."),
    ("Quel est le plus long fleuve du monde ?", "Le Nil est généralement considéré comme le plus long fleuve du monde."),
    ("Combien de fuseaux horaires y a-t-il en Russie ?", "La Russie s'étend sur 11 fuseaux horaires."),
    ("Quel est le plus petit os du corps humain ?", "Le plus petit os du corps humain est l'étrier, situé dans l'oreille moyenne."),
    ("Qui a composé la 'Sonate au Clair de Lune' ?", "La 'Sonate au Clair de Lune' a été composée par Ludwig van Beethoven."),
    ("Quelle est la plus grande espèce d'ours ?", "La plus grande espèce d'ours est l'ours polaire."),
    ("Combien de touches y a-t-il sur un piano standard ?", "Un piano standard a 88 touches."),
    ("Quelle est la capitale de l'Australie ?", "La capitale de l'Australie est Canberra."),
    ("Qui a écrit 'Gatsby le Magnifique' ?", "Gatsby le Magnifique a été écrit par F. Scott Fitzgerald."),
    ("Quel est le point le plus profond de l'océan ?", "Le point le plus profond de l'océan est la fosse des Mariannes, dans la fosse Challenger."),
    ("Combien y a-t-il de joueurs dans une équipe de football ?", "Une équipe de football a 11 joueurs sur le terrain."),
    ("Quel est le gaz le plus abondant dans l'atmosphère terrestre ?", "Le gaz le plus abondant dans l'atmosphère terrestre est l'azote."),
    ("Qui a peint le plafond de la Chapelle Sixtine ?", "Le plafond de la Chapelle Sixtine a été peint par Michel-Ange."),
    ("Quel est le plus grand organe du corps humain ?", "Le plus grand organe du corps humain est la peau."),
    ("Combien de faces a un cube ?", "Un cube a six faces."),
    ("Quelle est la capitale du Canada ?", "La capitale du Canada est Ottawa."),
    ("Qui a écrit 'Orgueil et Préjugés' ?", "Orgueil et Préjugés a été écrit par Jane Austen."),
    ("Quel est le plus petit pays du monde ?", "Le plus petit pays du monde est le Vatican."),
    ("Combien de chromosomes les humains ont-ils ?", "Les humains ont 23 paires de chromosomes, soit un total de 46."),
    ("Quel est le plus grand oiseau du monde ?", "Le plus grand oiseau du monde est l'autruche."),
    ("Qui a inventé l'ampoule électrique ?", "Thomas Edison est crédité de l'invention de la première ampoule électrique commercialement viable."),
    ("Quel est le mot le plus long de la langue française ?", "Le mot le plus long en français est 'anticonstitutionnellement', avec 25 lettres."),
    ("Combien d'éléments y a-t-il dans le tableau périodique ?", "Il y a actuellement 118 éléments dans le tableau périodique."),
    ("Quelle est la capitale de l'Espagne ?", "La capitale de l'Espagne est Madrid."),
    ("Qui a écrit 'Hamlet' ?", "Hamlet a été écrit par William Shakespeare."),
    ("Quelle est la plus grande île du monde ?", "Le Groenland est la plus grande île du monde."),
    ("Combien de pattes a une araignée ?", "Une araignée a huit pattes."),
    ("Quel est l'ingrédient principal du houmous ?", "L'ingrédient principal du houmous est le pois chiche."),
    ("Qui a peint 'La Persistance de la mémoire' ?", "La Persistance de la mémoire a été peinte par Salvador Dalí."),
    ("Quelle est la substance naturelle la plus dure sur Terre ?", "La substance naturelle la plus dure sur Terre est le diamant."),
    ("Combien de côtés a un hexagone ?", "Un hexagone a six côtés."),
    ("Quelle est la capitale de l'Égypte ?", "La capitale de l'Égypte est Le Caire."),
    ("Qui a écrit 'Guerre et Paix' ?", "Guerre et Paix a été écrit par Léon Tolstoï."),
    ("Quel est le plus grand félin ?", "Le plus grand félin est le tigre."),
    ("Combien de dents a un chien adulte ?", "Un chien adulte a généralement 42 dents."),
    ("Quelle est la langue principale parlée en Argentine ?", "La langue principale parlée en Argentine est l'espagnol."),
    ("Qui a découvert la gravité ?", "Sir Isaac Newton est crédité de la découverte de la gravité."),
    ("Quel est le plus petit océan ?", "Le plus petit océan est l'océan Arctique."),
    ("Combien d'étoiles y a-t-il sur le drapeau américain ?", "Le drapeau américain a 50 étoiles."),
    ("Quelle est la capitale de l'Italie ?", "La capitale de l'Italie est Rome."),
    ("Qui a écrit 'L'Odyssée' ?", "L'Odyssée est attribuée au poète grec antique Homère."),
    ("Quel est le plus grand oiseau volant ?", "Le plus grand oiseau volant par envergure est l'albatros hurleur."),
    ("Combien y a-t-il de continents ?", "Il y a sept continents."),
    ("Quel est l'ingrédient principal des sushis ?", "L'ingrédient principal des sushis est le riz vinaigré."),
    ("Qui a inventé le téléphone ?", "Alexander Graham Bell est crédité de l'invention du téléphone."),
    ("Quel est le plus grand astéroïde de la ceinture d'astéroïdes ?", "Le plus grand astéroïde de la ceinture d'astéroïdes est Cérès."),
    ("Combien de lunes Mars a-t-elle ?", "Mars a deux lunes : Phobos et Déimos."),
    ("Quelle est la capitale de la Chine ?", "La capitale de la Chine est Pékin."),
    ("Qui a écrit 'L'Attrape-cœurs' ?", "L'Attrape-cœurs a été écrit par J.D. Salinger."),
    ("Quelle est la plus grande espèce de requin ?", "La plus grande espèce de requin est le requin-baleine."),
    ("Combien d'os y a-t-il dans la main humaine ?", "Il y a 27 os dans la main humaine."),
    ("Quelle est la langue principale parlée en Allemagne ?", "La langue principale parlée en Allemagne est l'allemand.")
]

df_english = pd.DataFrame(english_qa_pairs, columns=['Question', 'Response'])
df_tunisian = pd.DataFrame(tunisian_qa_pairs, columns=['Question', 'Response'])
df_french = pd.DataFrame(french_qa_pairs, columns=['Question', 'Response'])

# Combine all DataFrames
df_all = pd.concat([df_english, df_tunisian, df_french], ignore_index=True)

# Save to CSV
df_all.to_csv('data\chatbot_data.csv', index=False)