# Step 1: Import necessary module
import random
# Step 2: Define word lists
subjects = [
    "Shahrukh Khan", "Salman Khan", "Amitabh Bachchan", "Akshay Kumar", "Ranveer Singh", "Virat Kohli",
    "MS Dhoni", "Sachin Tendulkar", "Cristiano Ronaldo", "Lionel Messi", "Captain Vikram Batra",
    "General Bipin Rawat", "Major Sandeep Unnikrishnan", "Field Marshal Manekshaw",
    "Captain Manoj Pandey", "Elon Musk", "Nikola Tesla", "Mokshagundam Visvesvaraya",
    "Sundar Pichai", "Satya Nadella", "Tim Cook", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg",
    "Barack Obama", "Donald Trump", "Joe Biden","Warren Buffett", "Oprah Winfrey", "Ellen DeGeneres",
    "Dwayne Johnson", "Chris Hemsworth", "Scarlett Johansson", "Jennifer Lawrence","Emma Watson", "Robert Downey Jr.",
    "Tom Holland", "Gal Gadot", "Chris Evans", "Beyoncé", "Taylor Swift", "Ariana Grande",
    "Kylie Jenner", "Kim Kardashian", "Rihanna", "Lady Gaga", "Bruno Mars"
    ]
verbs = [
    "discovers", "bans", "approves", "invents", "launches", "announces", "eats", "fights with", "dances with", "marries",
    "runs from", "hides", "destroys", "creates", "cooks", "sells", "buys", "paints", "builds", "breaks",
    "steals", "gives", "teaches", "learns", "wins", "loses", "catches", "throws", "pushes", "pulls",
    "jumps over", "flies with", "sings to", "screams at", "hugs", "kisses", "arrests", "saves", "rescues",
    "shoots", "chases", "laughs at", "cries with", "argues with", "replaces", "upgrades", "downloads", "uploads", "hacks",
    "controls", "designs", "programs"
]
objects = [
    "chocolate-powered car", "time travel machine", "AI president", "flying school", "robot teachers",
    "invisible phones", "banana rocket", "talking shoes", "singing laptop", "crying robot",
    "flying cows", "magic mirror", "pizza factory", "smart pillow", "haunted camera", "dancing bike",
    "laughing fridge", "dream machine", "super shoes", "chocolate rain", "alien spaceship",
    "underwater city", "golden toilet", "smart pen", "ice cream rocket", "ghost computer",
    "sleeping bus", "magical book", "fire-breathing drone", "bubblegum tower", "rocket-powered sofa",
    "singing umbrella", "dancing microwave", "rainbow bridge", "exploding sandwich", "robotic cow",
    "giant donut", "virtual dog", "teleporting cat", "chocolate fountain", "pizza planet",
    "banana boat", "superhero chicken", "angry calculator", "invisible chair", "moon elevator",
    "electric banana", "crying TV", "AI girlfriend", "robot baby", "hologram city"
]
adjectives = [
    "shocking", "bizarre", "unbelievable", "crazy", "funny", "strange", "weird", "wild", "unexpected", "amazing",
    "mysterious", "epic", "silly", "dangerous", "magical", "ridiculous", "surprising", "dramatic", "futuristic", "ancient",
    "legendary", "scary", "hilarious", "awkward", "naughty", "powerful", "useless", "lazy", "hyper", "secret",
    "strange-looking", "glittering", "shiny", "smelly", "noisy", "quiet", "haunted", "spicy", "tasty", "boring",
    "exciting", "unusual", "weirdest", "fastest", "slowest", "cursed", "blessed", "electric", "invisible", "rare"
]

# Step 3: Define function to generate one headline
def generate_headline():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    adjective = random.choice(adjectives)
    headline = f"{subject} {verb} a {adjective} {object}."
    return headline
# Step 4: Generate and print multiple headlines
n = int(input("How many headlines would you like to generate? "))

# Step 5: Loop to generate multiple headlines
for i in range(n):
    print(generate_headline())

    
# Stretch Features (Future)
# - Allow user to add custom words to subjects/verbs/objects
# - Save generated headlines into a text file
# - Add a GUI with buttons to generate new headlines