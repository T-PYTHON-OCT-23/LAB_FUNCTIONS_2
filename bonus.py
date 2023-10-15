'''
# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
'''

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