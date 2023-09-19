def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    price = d[1:]
    return float(price)

def percent_to_float(p):
    tip_percent = p[:-1]
    return float(int(tip_percent) / 100)

main()
