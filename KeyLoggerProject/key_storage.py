# store private keys here

import bcrypt
import hashlib
import json
import hasher

storage = {
    "John": hasher.encryption("password"),
    "Mary": hasher.encryption("password1"),
    "Katy": hasher.encryption("Password")
}


storage_encryption = {
    hasher.encryption("password"): "John",
    hasher.encryption("password1"): "Mary",
    hasher.encryption("Password"): "Katy"
}


storage_hash = {
    "John": hasher.strong_hash("password"),
    "Mary": hasher.strong_hash("password1"),
    "Katy": hasher.strong_hash("Password")
    } 





def dict_hash(): # A demo on hashing the dictonary
    dict_string = json.dumps(storage, sort_keys=True)
    return hash(dict_string)
# Issue - a new hash is generated every time


