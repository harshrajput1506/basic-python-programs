string = input('Enter line: ')
length = len(string)
string2 = ''
i = 0
while i < length:
    if i == 0:
        string2 += string[0].upper()
        i += 1
        continue
    elif string[i] == ' ':
        string2 += string[i]
        string2 += string[i+1].upper()
        i += 2
        continue
    elif string[i] != ' ':
        string2 += string[i]
        i += 1
print(string2)
