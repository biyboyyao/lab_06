def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

# Yaotian Zhang
def encoder(password):
    value = str()
    for i in password:
        num = int(i) + 3
        if num >= 10:
            num = num - 10
        value += str(num)
    return value

def decoder(password):
    ans = str()
    for i in password:
        num = int(i) - 3
        if num < 0:
            num += 10
        ans += str(num)
    return ans

def main():
    while True:

        menu()

        operation = int(input("Please enter an option: "))

        if operation == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")

        if operation == 2:
            print(f"The encoded password is {encoder(password)}, and the original password is {decoder(encoder(password))}.")

        if operation == 3:
            break

if __name__ == "__main__":
    main()
