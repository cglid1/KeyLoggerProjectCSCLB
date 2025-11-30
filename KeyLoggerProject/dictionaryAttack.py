# Will attempt to use a dictionary to guess passwords for password cracking
# Later may implement a way to guess the password in the key_storage dictionary lists
import time, key_storage


class DictionaryAttack:

    def dictionary_attack(self):
        print(key_storage.basic_storage)

dictionaryAttack = DictionaryAttack()
dictionaryAttack.dictionary_attack()