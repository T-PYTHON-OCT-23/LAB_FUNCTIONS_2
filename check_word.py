def check_word(word:str)->str:
    for char in word:
        n=""
        if word.isalpha():
            #print(f" {word.lower()}",end=" ")
            for char2 in char:
                if char2.isupper():
                    print(n,char2.lower(),end="")
                else:            
                    print(char,end="")
sentence = input("please enter your sentence: ")                                            
check_word(sentence)