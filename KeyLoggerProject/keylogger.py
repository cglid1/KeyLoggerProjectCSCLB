# run code here
import key_storage
import hasher


class Keylogger:

    
    
    
    
    # A basic comparsion between user input and stored data
    
    
    ''' def verification(self):
        print(hasher.verify_hash(key_storage.storage, hasher.stored_hash))
        return key_storage.storage, hasher.strong_hash '''
    
    def code_verification(self): # This function verifies that the password strings in the storage dictionary are encrypted
        print(key_storage.storage)

    def log(self): # Function that requests for user name and password
             
        
        
        while True:
            user_name = input("Please enter your username: ")
          #  print(key_storage.dict_hash()) # run time issued hash for testing purposes
            if user_name in key_storage.storage: # If statement comparing user input to the dictonary
                encrypted_password = key_storage.storage[user_name] # Stores the password encrypted string
                decrypted_password = hasher.decryption(encrypted_password) 
                print("Password: " + decrypted_password)
                break
            else:
                __password_export = input("Password not found.\nWould you like to add to the list? (y/n) ").lower() # Allows user to add and save password in memory
                                                                                                                # Memory meaning it's doesn't modify the key_storage file
                if __password_export == "y":
                    password = input("Please enter a password: ")
                    encrypted_password = hasher.encryption(password)
                    key_storage.storage[user_name] = encrypted_password   # Where the user name and password are sent to the dictonary to be stored
                    decrypted_password = hasher.decryption(encrypted_password)
                    continue
                elif __password_export == "n":    # Promptly ends the loop
                    print("Goodbye!")
                    break
    
    
    def hash_log(self): # A variation that hashes the passwords before storing it
        while True:
            user_name = input("Please enter your username: ")
            print(key_storage.dict_hash()) # run time issued hash for testing purposes
            if user_name in key_storage.storage: # If statement comparing user input to the dictonary
                print("Password: " + key_storage.storage[user_name])
                break
            else:
                __password_export = input("Password not found.\nWould you like to add to the list? (y/n) ").lower() # Allows user to add and save password in memory
                                                                                                                # Memory meaning it's doesn't modify the key_storage file
                if __password_export == "y":
                    password = input("Please enter a password: ")
                    encrypted_password = hasher.strong_hash(password)
                    key_storage.storage[user_name] = encrypted_password   # Where the user name and password are sent to the dictonary to be stored
                    continue
                elif __password_export == "n":    # Promptly ends the loop
                    print("Goodbye!")
                    break


    



keylogger = Keylogger() # keylogger is the blueprint, Keylogger() is the creation (allows the functions to be ran like the following)
keylogger.code_verification() # This calls the code_verification function to be ran (just a visual image to show the encryption)
keylogger.log() # This calls the log function to be ran (deals with user name and password encryption)
# keylogger.hash_log() # This calls the hash_log function to be ran (hashes the passwords stored in the dictionary)
