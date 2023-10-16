def captlize (words:str):
     isinstance(words,str)
     space=" "
     for i in words:
        if i.isupper():
            space=f"{space}  {i.lower()}"
        else:
            space = space+i

     return space
    
    
words = input("enter the word: ")
result:str =str(captlize(words))
# captlize(words)
print(result)