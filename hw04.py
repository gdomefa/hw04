# ------------------------------------------------------
#        Name: (Gloria Domefa)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Gets a sentence from the user and gives different output depending on the user's input 
        If the user uses the secret word it prints You used the secret word!
        If the user uses the words dog or Dog it prints You used the word "dog"
        or the word "Dog"! by including backslash in the print statement
        If it has neither it prints Try again! and reruns the loop """
   # Get input from user
    while (True):
       user_sentence = input("Give me a sentence: ")
       
       # Check if key word is used
       if secret_word in user_sentence:
           print("You used the secret word!")
           #end loop
           break
        
       # Check if dog or Dog is used
       elif "dog" in user_sentence or "Dog" in user_sentence:
           print("You used the word \"dog\" or the word \"Dog\"!")
           break

       # If neither are true, print try again and rerun the loop
       else:
           print("Try again")

    
        
# Task 2
def check_greater():
    """ Gets two integer inputs from the user
        Tells the user which number is greater
        If they're equal, it prints Try again and reruns the loop"""
    while (True):
        num1 = input("Give me a first integer: ")
        num2 = input("Give me a second integer: ")
        #First integer greater than second: prints First is Greater
        if num1 > num2:
            print("First is Greater")
            break
        # Second integer greater than first: prints Second is Greater
        elif num2 > num1:
            print("Second is Greater")
            break
        # Integers are equal, prints Try again and repeat body of the loop
        else:
            print("Try again")



# Task 3
def get_special_numbers():
    """ A for loop to examine numbers 1-40 and print based on criteria:
        must be odd, a multiple of 3, and not a multiple of 5"""
    for n in range(1,41):
        # The number is odd
        if n % 2 == 1:
            # The number is a multiple of 3
            if n % 3 == 0:
                # The number is not a multiple of 5
              if n % 5 != 0:
                  print(n)



# Task 4.a
def my_for_loop():
    """ Asks for a string from the user
        Uses len function to see if the string is in range [2,5]
        Function immediately returns if there are spaces
        Checks each letter in the string
        If the input is a valid length and a vowel, it prints 'letter <let> is a vowel'
        If the input is a valid length and a consonant, it prints 'letter <let> is a consonant'
        """
    user_string = input("Give me a string: ")
    vowel = ["a","e","i","o","u"]
    con = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    #for x in range(1,6):
        #if len(user_string) in range(1,6):
            #print("testing")

# Task 4.b
def my_while_loop():
    """ Offers the user three choices (a b or c)
        Different outcomes for inputs
        a: the while loop repeats
        b: print goodbye and return
        c: exits program
        none: prints 'try again' and repeats the while loop"""
    while (True):
        option = input("Choose one option: a, b, or c: ")
        #if the user selects a, the menu repeats
        if option == "a":
            continue
        
        #if the user selects b, the function prints "Goodbye" and return
        if option == "b":
            print("Goodbye")
            return
        
        #if the user selects c, the program should exit immediately
        if option == "c":
            sys.exit()
        
        #if any other letter is selected, the loop prints "try again" and repeats
        else:
            print("try again")
            
        

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
