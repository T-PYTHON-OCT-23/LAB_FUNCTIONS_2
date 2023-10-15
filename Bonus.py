def seprate_sentence(sentence : str) -> str:
    new_sentence=""
    if type(sentence)== type(""):
        for char in sentence:
            if char.isupper():
                new_sentence += " "
                
            new_sentence+= char
    else:return "Enter only letters"
    return new_sentence.lower()



sentence= seprate_sentence("helloWorldThere")

print(sentence)