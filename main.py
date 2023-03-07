import hashlib
import sys

password = input("Enter your password: ")
parameter = sys.argv[1]

# Encode password and parameter as UTF-8
password = password.encode('utf-8')
parameter = parameter.encode('utf-8')

# Combine password and parameter and hash using SHA256
hashed_value = hashlib.sha256(password + parameter).hexdigest()

print("Hashed value: " + hashed_value)
