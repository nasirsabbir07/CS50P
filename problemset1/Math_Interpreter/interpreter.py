def main():
    expression = input("Expression: ").strip()
    expression_list = expression.split(' ')
    x = expression_list[0]
    z = expression_list[2]
    y = expression_list[1]
    interpreter(x,y,z)

def interpreter(x,y,z):
    oparend_a = int(x)
    oparend_b = int(z)
    operator = y

    if(operator == '+'):
        sum = oparend_a + oparend_b
        print(f" {sum:.1f}")

    elif(operator == '-'):
        deduct = oparend_a - oparend_b
        print(f" {deduct:.1f}")

    elif(operator == '*'):
        product = oparend_a * oparend_b
        print(f" {product:.1f}")

    else:
        division = oparend_a / oparend_b
        print(f" {division:.1f}")

main()
