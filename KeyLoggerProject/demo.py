import passwordCracker, key_storage, dictionaryAttack, time
from passwordCracker import passwordCracker
class Demo:
    
    # while True:
    #     user_name = passwordCracker.dictionary_Cracker(key_storage.basic_storage)
    #     if user_name in key_storage.basic_storage:
    #         print("Password: " + key_storage.storage[user_name])
    #         break
    #     else:
    #         continue

    def login(username, password, correct_user, correct_pass):
        return username == correct_user and password == correct_pass
    
    

    @staticmethod
    def brute_force_username():
        start = time.time()
        for guess in passwordCracker.word_gen():
            if guess in key_storage.basic_storage:
                end = time.time()
                clock = str(end - start)
                print(f"Username found: {guess}")
                print(f"Cracking took {clock} seconds.")
                return guess
        print("No username found.")
        return None
    
    @staticmethod
    def brute_force_password(found_user):
        
        if found_user is None:
            print("Cannot brute-force password: Username not found.")
            return None
        
        
        password_toCrack = key_storage.basic_storage[found_user]
        start = time.time()
        
        
        for guess in passwordCracker.word_gen():
            
            if guess == password_toCrack:
                end = time.time()
                clock = str(end - start)
                print(f"Password found: {guess}")
                print(f"Password cracking took {clock} seconds.")
                return guess
   



demo = Demo()
found_user = demo.brute_force_username()
demo.brute_force_password(found_user)
