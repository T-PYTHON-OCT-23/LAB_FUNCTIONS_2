

def word_string(input_string):
    result = ""
    for char in input_string:
        if char.isupper() :
            result += " " + char.lower()
        else:
            result += char
    return result

input_value = "alyaSanhanAlsuhimi"

print(word_string(input_value))


'''function it takes strin parametter.

   is done.

'''