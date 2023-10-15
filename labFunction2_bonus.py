def replace_split(word:str):
    if isinstance(word,str):
       for i in word:
           if i.isupper():
               word.split()
    print(f"after split: {word.lower()}")
               
       #splitWord =  re.findall(r'[A-Z][a-z]*', word)
       #splitWord = splitWord.lower()
      # splitWord = word.split()
    #print(f"after split {word}")
        

  

words = "helloWorldThere"
print("befor split: "+ words)
replace_split(words)