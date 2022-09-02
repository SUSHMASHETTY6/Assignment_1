

# How many unique words have been used in the sentence?use the split methods and set to get the unique words
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split(" ") # split method()
print("Number of unique words: ", len(set(words))) # Set method()
