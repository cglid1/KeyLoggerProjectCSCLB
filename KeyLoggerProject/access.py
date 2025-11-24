# Tried to sort through the dictionary using the password instead
# It isn't possible because users can have the same password


import key_storage

class Access:
    
    
        
    
        def login(self):
            while True:
            
                password_input = input("Enter password: ")
                stored_password = key_storage.storage.get(password_input)
                if stored_password == key_storage.storage.get(password_input):
                    print("Hello" + key_storage.storage[password_input])
                    break
                else:
                    print("Goodbye")
                    
        

access = Access()    
access.login()

