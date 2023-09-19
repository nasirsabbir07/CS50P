gqol = "What is the Answer to the Great Question of Life, the Universe, and Everything?"
print(gqol)
answer = input("Give answer...").lower().strip()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
