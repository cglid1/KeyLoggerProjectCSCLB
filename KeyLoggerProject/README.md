# List Ideas Here:
1.) Have a file with the most common passwords and compare it to a dictionary of stored passwords. 

2.) If you want to search the dictionary list by password, you have to give each username and password a unique hash. 

3.) Might add a function that asks for username and password like a tradition login for penetration testing (specifically brute force). 

4.) Built dictionary that saves passwords as hashes, and hashes the password before sending it. 

5.) Need to try having a set key for encryption to compare user input to dictionary (two different keys are used between compile and run time). 

6.) Next I will try to first hash all password entries then encrypt them for max security.

7.) Hashing the dictionary set passwords vs hashing the user entered password end up with different results likely due to 
a key being generated two different time to hash those passwords.

8.) Could try a login setup that doesn't include a password, and instead generates a code after entering their username.