# Reverse a Sentence
# Write a function named reverseSentence that takes a sentence (a string containing words separated by spaces) as input and returns the sentence with its words reversed.
# Sample Input: "Hello World" Sample Output: "olleH dlroW"
def reverseSentence(sentence):
    words = sentence.split()  
    reversed_words = [word[::-1] for word in words]  
    reversed_sentence = " ".join(reversed_words)  
    return reversed_sentence

# Test the function
input_sentence = "Hello World"
output = reverseSentence(input_sentence)
print("Output:", output) 