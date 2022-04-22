def translate(phrase):
    word=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                word=word+'G'
            else:
                word=word+'g'
        else:
            word=word+letter

print(translate(input("enter word")))

# multiple line comments
"""
comments
"""