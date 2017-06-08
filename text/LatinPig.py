def LatinPig(stringA):
    vowel='aeiou'
    for index in range(len(stringA)):
        if stringA[index] not in vowel:
            return stringA[:index]+stringA[index+1:]+stringA[index]+'ay'
            
#print(LatinPig('banana'))