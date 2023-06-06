import random


def get_random_number():
    return random.randint(100, 1000)


def bagel():
    x = get_random_number()
    # print(x)

    tries = 1

    while tries < 11:
        y = int(input("Guess the secret number: "))
        if y > 1000 or y < 100:
            print("================================")
            print("⚠️⚠️  Number must be in Range 100 - 999 ⚠️⚠️")
            print("================================")

        else:
            if x != y:
                x_string = str(x)
                y_string = str(y)
                if (
                    x_string[0] == y_string[0]
                    or x_string[1] == y_string[1]
                    or x_string[2] == y_string[2]
                ):
                    print("FERMI")
                elif (
                    x_string[0] == y_string[1]
                    or x_string[0] == y_string[2]
                    or x_string[1] == y_string[0]
                    or x_string[1] == y_string[2]
                    or x_string[2] == y_string[0]
                    or x_string[2] == y_string[1]
                ):
                    print("PICO")
                else:
                    print("BAGELS")

            else:
                print("Correct!")
                break

        tries += 1

    print(f"It took you {tries} tries")


if __name__ == "__main__":
    bagel()
