def encoder(password):
    value = str()
    for i in password:
        num = int(i) + 3
        if num >= 10:
            num = num - 10
        value += str(num)
    return value

def decoder(password):
    print("Walter White")
