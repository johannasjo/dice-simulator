'''
• Be användaren om ett val av hur många tärningar som skall kastas och ta emot 
  den informationen när den trycks in. Minst 1 och max 4 tärningar skall väljas av användaren.

• Programmet slumpar resultat för varje enskild tärning, en i taget, 
  och skriver ut detta på skärmen tillsammans med summan av slagna tärningar hittills.

• Om någon tärning får resultatet 1 så adderas detta inte till summan, 
  utan två nya tärningar slås. Detta ska framgå av text på skärmen när/om det sker. 
  Så länge någon tärning får resultatet 1 upprepas denna procedur.

• När alla tärningar är slagna skrivs totalsumman samt antal tärningsslag ut på skärmen.

• Spelaren får alternativ att börja om eller avsluta programmet.'''

import random

def print_line():
    print("\n") 

def introduction():
    name = "Johanna Sjöstrand "
    date = "24/4/2020"

    print (name + date)
    print_line()


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

def throw_dice():
    return random.randint(1, 6)


def play_dice(amount_of_die):
    '''
    1. Programmet slumpar resultat för varje enskild tärning, en i taget, 
      och skriver ut detta på skärmen tillsammans med summan av slagna tärningar 
      hittills. 
    2. Om någon tärning får resultatet 1 så adderas detta inte till summan, 
       utan två nya tärningar slås. Detta ska framgå av text på skärmen när/om det sker. 
       Så länge någon tärning får resultatet 1 upprepas denna procedur.''' 
    total_sum = 0 
    throw_number = 0
    while throw_number < amount_of_die:
        input("Kasta tärning? Tryck enter när du är redo!")
        value_of_dice = throw_dice()
        throw_number += 1
        
        if value_of_dice == 1:
            amount_of_die += 2
            print ("Du slog en 1:a, då får du slå två nya tärningar!")
        
        else:
            total_sum += value_of_dice 
            print("Du kastade: " + str(value_of_dice))

        print (throw_number)
        print (amount_of_die)
        print_line() 
        print("Den totala summan av kastade tärningar är: " + str(total_sum)) 






def main():
    introduction()
    #amount_of_die = choose_amount_of_die()
    print (play_dice(2))
  


if __name__ == "__main__":
    main() 