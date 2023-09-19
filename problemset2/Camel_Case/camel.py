user_input = input("camelCase: ")

character_list = []

for letter in user_input:
    character_list.append(letter)
# print(len(character_list))

keys = []
values = []
for i in range(65,91):
    keys.append(chr(i))
    values.append("_" + chr(i + 32))

# print(values)

character_dict = dict(zip(keys, values))

# print(character_dict)
for i in range(len(character_list)):
    if(character_list[i] in character_dict):
        character_list[i] = character_dict[character_list[i]]

python_convention = "".join(character_list)
print(f"snake_case: {python_convention}")

