text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

new_text = text.split() 
lengths = list(map(len, new_text)) 
print(lengths)
