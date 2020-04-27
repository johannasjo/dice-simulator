import random

def print_line():
    print("\n") 

def introduction():
    name = "Johanna Sjöstrand "
    date = "27/4/2020"

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
# Will randomize number of the dice when called
    return random.randint(1, 6)


def play_dice(amount_of_die):
 # Will ask to throw dice until the input number of die is reached, 
 # add 2 die if the value is 1 and return and print the result
    total_sum = 0 
    throw_number = 0
    while throw_number < amount_of_die:
        input("Kasta tärning? Tryck enter när du är redo!")
        print_line()
        value_of_dice = throw_dice()
        throw_number += 1
        
        if value_of_dice == 1:
            amount_of_die += 2
            print ("Du slog en 1:a, då får du slå två nya tärningar!") 
            print ("Ettan räknas inte in i slutsumman.")
            print_line()
        
        else:
            total_sum += value_of_dice 
            print("Du kastade: " + str(value_of_dice))
       
        print_line() 
        print("Summan av kastade tärningar är: " + str(total_sum))
        print_line() 
    return throw_number, total_sum
    
  


#Function will ask player if they want to play again when called 
#Can only answer 'j' or 'n'

def ask_continue():
    while True:
        answer = input("Vill du spela igen? (j/n): ")
        if answer == 'j':
            return True
        elif answer == 'n':
            return False

def main():
    introduction()
    while True:
        amount_of_die = choose_amount_of_die()
        amount_of_throws, total_sum = play_dice(amount_of_die)
        print("Det totala antalet tärningsslag blev: " + str(amount_of_throws))
        print("Totalsumman för denna spelomgång blev: " + str(total_sum)) 
        print_line()
            
        answer = ask_continue()
        if not answer:
            break         
          
    print("Tack för den här spelomgången! Kom gärna tillbaka imorgon!")
     
         
if __name__ == "__main__":
    main()