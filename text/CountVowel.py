def CountVowel(stringA):
    vowel = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for character in stringA:
        if character.lower() in vowel:
            vowel[character.lower()] = vowel[character.lower()]+1
    return vowel


#print(CountVowel("qwertyuiopasdfghjklzxcvbnm,"))
    