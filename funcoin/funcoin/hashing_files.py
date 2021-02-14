from hashlib import sha256
import os
folder = os.getcwd()
# print(folder)
file_path = folder+'/funcoin/one_dollar_bill.jpg'
# print(file_path)
file = open(file_path, "rb")
hash = sha256(file.read()).hexdigest()
file.close()

print(f"The hash of my file is: {hash}")
