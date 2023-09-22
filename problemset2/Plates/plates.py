def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate_len = len(s)
    if((2 <= plate_len <= 6) and s.isalnum()):
        if(s[:].isalpha()):
            return True
        if(s[0:2].isalpha()):
            for i in range(2, plate_len-1):
                if(s[i].isdigit()):
                    if((s[i] == "0") or (s[i+1].isalpha())):
                        return False
                elif(s[i].isalpha() and s[i+1] == "0"):
                    return False
            return True
        else:
            return False
    else:
        return False

main()
