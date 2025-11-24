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



        # for username, _ in key_storage.basic_storage:
        #     if username == correct_user:
        #         crackedUser = username
        #         print(f"Correct username: {crackedUser}.")



    



demo = Demo()
demo.brute_force_username()

