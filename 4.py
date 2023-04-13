def encrypt(str, key):
    return key.join(str)
def decrypt(str, key):
    return str.split(key)
#-main-

mainString = input("Enter string - ")
encryptKey = input("Enter encryption key - ")

enStr = encrypt(mainString, encryptKey)
decLst = decrypt(mainString, encryptKey)  #Returns List

#decLst is a list, now convert into string.

decStr = "".join(decLst)
print("The encrypted string is", enStr)
print("The decrypted string is", decStr)
