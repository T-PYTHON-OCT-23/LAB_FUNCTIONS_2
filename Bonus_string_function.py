def string_func(sentence:str):
    if isinstance(sentence,str):
        value=""
        print("The word is string.")
        value1 = print("The word in lowercase: ",sentence.lower())
        for word in sentence:
            if word.isupper():
                value= value+" "+word.lower()
            else:
                value+=word
    print("The sentence: ",value)

sentence = input("Enter a sentence:")
string_func(sentence)
