import hashlib
str= input("Enter the string : ")
output = hashlib.md5(str.encode())
print("String to MD5 : ", end ="")
print(output.hexdigest())