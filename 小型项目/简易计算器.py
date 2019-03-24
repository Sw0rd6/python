def main():
    while True:
        sign1 = input()
        if "+" in sign1:
            if sign1[0] != "+":
                a = sign1.index("+")
                left, right = int(sign1[0:a]), int(sign1[a+1:])
                Sum = left + right
                print(Sum)
            else:
                Sum += int(sign1[1:])
                print(Sum)
        if "-" in sign1:
            if sign1[0] != "-":
                a = sign1.index("-")
                left, right = int(sign1[0:a]), int(sign1[a+1:])
                Sum = left - right
                print(Sum)
            else:
                Sum -= int(sign1[1:])
                print(Sum)
        if "*" in sign1:
            if sign1[0] != "*":
                a = sign1.index("*")
                left, right = int(sign1[0:a]), int(sign1[a + 1:])
                Sum = left * right
                print(Sum)
            else:
                Sum *= int(sign1[1:])
                print(Sum)
        if "/" in sign1:
            if sign1[0] != "/":
                a = sign1.index("/")
                left, right = int(sign1[0:a]), int(sign1[a+1:])
                Sum = left / right
                print(Sum)
            else:
                Sum /= int(sign1[1:])
                print(Sum)
        if sign1 == "q":
            break
if __name__ == "__main__":
    main()
