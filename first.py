import random
import string

# define the password length
length = 12

# define the characters to use in the password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# combine the characters
all_characters = lowercase + uppercase + digits + symbols

# randomly select characters from the combined list
password = ''.join(random.sample(all_characters, length))

# print the generated password
print(password)
