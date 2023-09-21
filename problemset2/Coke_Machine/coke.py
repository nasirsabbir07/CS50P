def main():
    price = 50
    print(f"Amount Due: {price}")

    accepted_values = [5, 10, 25]
    change = 0

    inserted_amount(price, accepted_values, change)

def inserted_amount(price, accepted_values, change):
    while(price > 0):
        payment = int(input("Insert Coin: "))
        if(payment in accepted_values):
            price = price - payment
            if(price < 0 or price == 0):
                print(f"Change Owed: {abs(price)}")
            else:
                print(f"Amount Due: {price}")
        else:
            print(f"Amount Due: {price}")

if __name__ == "__main__":
    main()
