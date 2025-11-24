# Initially a basic brute force entry using a static variable

import time # Will be used to determine how long the password cracker took
class passwordCracker:
    all_chars = r""" !"#\$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ """
    basic_char = "abcdefghijklmnopqrstuvwxyz"
    except_specialChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    capital_Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    
    
    
    
    @staticmethod
    def word_gen(except_specialChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
        length = 1
        while True:
            a = [i for i in except_specialChar]
            for y in range(length - 1):
                a = [x + i for i in except_specialChar for x in a]

            for attempt in a:
                yield attempt
            
            length += 1
    
    
    
    
    

    
    
    def password_cracker(self, except_specialChar):
        
        password = input("Enter password: ")
        start = time.time()

        
        print(except_specialChar)
        attempt = []
        foundPassword = None

        for val in range(5):
            a = [i for i in except_specialChar]
            for y in range(val):
                a = [x + i for i in except_specialChar for x in a]
        
            for attempt in a:
                if attempt == password:
                    foundPassword = attempt
                    break

            if foundPassword:
                break  

        

        end = time.time()
        clock = str(end - start)

        print("Your Password: " + foundPassword)
        print("Time taken: " + clock + " seconds")




