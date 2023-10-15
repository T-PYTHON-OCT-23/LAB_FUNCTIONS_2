def string_functhion(text:str):
    if(type(text)==str):
        new_string=""
        for char in text:
            if char.isupper():
                new_string+=" "+char.lower()
            else:
                new_string+=char
    print(new_string)

        
    
string_functhion('helloWorldThere')