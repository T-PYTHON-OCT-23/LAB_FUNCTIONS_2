def string_functhion(name:str):
    if(type(name)==str):
        for i in name:
            if i.upper():
                i.lower()
        return print(name)
    
string_functhion('helloWorldThere')