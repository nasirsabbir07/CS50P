def main():
    txt = input("Write something containing emoticons, ")
    print(convert(txt))

def convert(user_input):
    slightly_smiley_face = "🙂"
    slightly_frowning_face = "🙁"
    # nested replace method
    res = user_input.replace(":)", "%temp").replace(":(",       slightly_frowning_face).replace("%temp", slightly_smiley_face)

    return res

main()
