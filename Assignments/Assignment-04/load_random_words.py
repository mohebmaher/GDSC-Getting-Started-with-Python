with open("random_words.txt", mode="rt") as text_file:
    random_words = text_file.read()

    
print("The first ten words:")
counter = 0
for word in random_words.split(" "):
    if counter <= 10:
        print(">>", word)
    counter += 1
    
print("*" * 20)
print(f"Number of words: {counter}")