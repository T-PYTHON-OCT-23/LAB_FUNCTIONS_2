def function(word:str) -> str:
    
    if word.isalpha() == True:
        new_word = ""
        for n in word:

            if n.isupper():
                new_word += " "
            else:
                new_word += n 
            if n.isupper():
                new_word += n.lower()
        return print(new_word)
    else:
        print("string plz1")

word = "helloWolrdThere"
function(word)