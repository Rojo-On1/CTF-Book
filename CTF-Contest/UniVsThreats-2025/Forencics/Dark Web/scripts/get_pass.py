from hashlib import md5
from string import printable

def hash_md5(password : str):
    hashlib = md5()
    hashlib.update(password.encode())
    return hashlib.hexdigest()

password = ""
chars = printable[:-5]
md5sums = open("../evidences/password_list").read().strip().split("\n")

breaked = 0
while breaked < len(md5sums):
    for char in chars:
        if hash_md5(password+char) == md5sums[breaked]:
            password += char
            breaked += 1
            break
    print(f"\rPassword: {password}",end="")
print("\n[+] Success.")
