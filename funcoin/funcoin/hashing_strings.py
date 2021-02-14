import hashlib

input_bytes = b"funcoin"
input2_bytes = b"Funcoin"

output = hashlib.sha256(input_bytes)
output2 = hashlib.sha256(input2_bytes)

# convert bytes to hex
print(output.hexdigest())
print(output2.hexdigest())
