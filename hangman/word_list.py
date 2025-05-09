words_with_hints = {
    "napoleon": "French emperor famously defeated at Waterloo.",
    "elephant": "The largest land animal with a trunk.",
    "pizza": "Popular Italian dish often topped with cheese.",
    "sunflower": "Tall yellow plant that turns to face the sun.",
    "sherlock": "Fictional detective known for logical reasoning.",
    "cleopatra": "Queen of Egypt, lover of both Julius Caesar and Mark Antony.",
    "koala": "Tree-dwelling marsupial from Australia.",
    "sushi": "Japanese dish often made with raw fish and rice.",
    "orchid": "Elegant flowering plant with over 28,000 species.",
    "batman": "Dark, brooding superhero who fights crime in Gotham."
}

def update_display(word, display, guess):
    return [guess if letter == guess else current for letter, current in zip(word, display)]

hangman = {
    0: (" o ", "/|\ ", "/ \ "),
    1: (" o ", "/|\ ", "/ "),
    2: (" o ", "/|\ ", " "),
    3: (" o ", "/| ", " "),
    4: (" o ", "/ ", " "),
    5: (" o ", " ", " "),
    6: (" ", " ", " ")
}