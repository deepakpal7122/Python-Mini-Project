import random
import string

pass_len = 8
charvalues = string.ascii_lowercase + string.digits + string.punctuation

# 1 logic
password = ""
for i in range(pass_len):
    password = password + random.choice(charvalues)

print("Your random password is :",password)

# 2 logic
# list comprehension [function for i in range(n)]
''' 
res = "".join([random.choice(charvalues) for i in range(pass_len)])
print(res)
'''
