def string_function(word_str):
     isinstance(word_str,str)
     string = ""
     for char in word_str:
         if char.isupper():
             string = string+ " " + char.lower()
         else:
             string = string + char
     return string
word_str = "helloWorldThere"   
result = str(string_function(word_str))  
print(result)       











'''
def sting_function(string1:str)->str:
    isinstance(string1,str)
    space =" "
    for word in string1:
        if word.isupper():
            space = space +" " =word.lower
        else:
            space=space+word 

    return space
w= "helloWorldThere"
w2:str=(sting_function(w))
print(w2)




def sting_function(string:str)->str :
    #string = "hello World There"
    word = string.split(' ')
    print(word[0].upper())
    #word2= word.lower
    #print(word2)

print(sting_function("helloWorldThere"))
'''