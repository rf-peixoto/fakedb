from hashlib import md5
from base64 import b64encode
from secrets import token_urlsafe
from random import choice

# Setup:
total = 2036
domain = "@domain.com"
tmp_list = []

# Files:
with open("first.txt", "r") as fl:
    first = fl.read().split("\n")
with open("last.txt", "r") as fl:
    last = fl.read().split("\n")

# Do it:
counter = 0
while counter <= total:
    try:
        # Email:
        name = choice(first).lower()[0]
        surname = choice(last).lower()
        email = "{0}{1}{2}".format(name, surname, domain)
        # Password:
        salt = token_urlsafe(16)
        salt64 = b64encode(salt.encode())
        password = md5(str(token_urlsafe(64) + salt).encode()).hexdigest()
        pass_pkt = ":{0},{1}".format(password, salt64.decode())
        # Append:
        tmp = email + pass_pkt
        tmp_list.append(tmp)
        print(tmp)
        counter += 1
    except:
        continue

# Save file:
with open("output.txt", "w") as fl:
    for i in tmp_list:
        fl.write(i + "\n")
print("Done.")
