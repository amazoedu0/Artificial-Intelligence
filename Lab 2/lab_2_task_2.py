sentence = input("\nEnter any sentence : ")
newList = sentence.split(" ")
finalList = []
vowel = ['a', 'e', 'i', 'o', 'u']
for word in newList:
    if word[0].lower() in vowel:
        word = word+'hay'
    else:
        temp = ""
        length = len(word)
        for i in range(1, length):
            letter = word[i-length]
            temp += letter
        temp += word[0]
        word = temp+"ay"
    finalList.append(word)
print(f"\nOutput : {finalList}\n")
