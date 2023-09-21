vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
user_input = input("Input: ")
word_list = []

for letter in user_input:
    word_list.append(letter)

# print(word_list)

for vowel in vowels:
    while (vowel in word_list):
        word_list.remove(vowel)

short_hand  = "".join(word_list)
print(f"Output: {short_hand}")
