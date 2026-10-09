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
    """ Add your docstring """
    pass



# Task 3
def get_special_numbers():
    """ Add your docstring """
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

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
