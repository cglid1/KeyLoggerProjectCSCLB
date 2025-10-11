# run code here
import key_storage
class Keylogger:

    
    
    
    
    # A basic comparsion between user input and stored data
    
    
    
    
    
    def log(self): # Function that requests for user name and password
             
        
        while True:
            user_name = input("Please enter your username: ")
        
            if user_name in key_storage.storage: # If statement comparing user input to the dictonary
                print("Password: " + key_storage.storage[user_name])
                break
            else:
                __password_export = input("Password not found.\nWould you like to add to the list? (y/n) ").lower() # Allows user to add and save password in memory
                                                                                                                # Memory meaning it's doesn't modify the key_storage file
                if __password_export == "y":
                    password = input("Please enter a password: ")
                    key_storage.storage[user_name] = password   # Where the user name and password are sent to the dictonary to be stored
                    continue
                elif __password_export == "n":    # Promptly ends the loop
                    print("Goodbye!")
                    break

keylogger = Keylogger() # keylogger is the blueprint, Keylogger() is the creation
keylogger.log() # Where the function is called so it can be ran
