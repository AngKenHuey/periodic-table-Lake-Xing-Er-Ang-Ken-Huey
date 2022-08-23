import random
def main():
    """Let's start guessing game"""
    print("Let's start guessing game")
    list=("Oxygen","Hydrogen","Helium")
    x=random.choice(list)
    guess=None
    
    while x !=guess:
        print("Hydrogen")
        print("Helium")
        print("Oxygen")
        
        guess= str(input("pick an elemant :"))
        
        
        if x==guess:
           print("You genius")
        elif x > guess:
            print("False,please try again")
                    
main()
            
        
        
 