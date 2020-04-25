def introduction():
    name = "Johanna Sjöstrand "
    date = "24/4/2020"

    print (name + date)
    print("\n")


def choose_amount_of_die():
    #Will ask user for input on amount of die, if text or wrong amount the loop will continue until answer is within the valid frame 
    while True:
        amount_of_die = input("Välj hur många tärningar du vill kasta, du kan välja mellan 1-4 tärningar: ")
        if not amount_of_die.isdigit():
            print ("Det är ingen siffra! Försök igen!")
            continue

        else:
            amount_of_die = int(amount_of_die)

        if not (amount_of_die >= 1 and amount_of_die <= 4):
            print ("Fel val av antal tärningar! Försök igen!")
            continue

        break
    return amount_of_die




def main():
    introduction()
    amount_of_die = choose_amount_of_die()
    print (amount_of_die)


if __name__ == "__main__":
    main() 