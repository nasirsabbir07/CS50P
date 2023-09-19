def main():
    time = input("What time is it? ")

    meal_time = convert(time)

    if(7.00 <= meal_time and meal_time <= 8.00):
        print("breakfast time")
    elif(12.00 <= meal_time and meal_time <= 13.00):
        print("lunch time")
    elif(18.00 <= meal_time and meal_time <= 19.00):
        print("dinner time")
    else:
        print("not meal time yet!")

def convert(time):
    time_list = time.split(":")
    hours = float(time_list[0])
    minutes = float(time_list[1])

    minutes_factor = minutes / 60.00
    meal_time_float = hours + minutes_factor

    return meal_time_float

if __name__ == "__main__":
    main()
