str = input("Enter a string - ")
vowels = 0
consonants = 0
upper = 0
lower = 0
vowelsLst = ['a', 'e', 'i', 'o', 'u']
consonantsLst = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 'x', 'c', 'v', 'b', 'n', 'm']
for i in str:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1

    for vowel in vowelsLst:
        if i.lower() == vowel:
            vowels += 1
            
    for consonant in consonantsLst:
        if i.lower() == consonant:
            consonants += 1
       
print("No. of Vowels is", vowels)
print("No. of Consonants is", consonants)
print("No. of lowercase is", lower)
print("No. of uppercase is", upper)

        
    

    
