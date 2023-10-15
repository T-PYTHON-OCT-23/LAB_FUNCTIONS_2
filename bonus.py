def b():
    m_string = "helloWorldThere"
    new_m="  "
    for i in range(len(m_string)):
        if (m_string[i].isupper() ):
             if (m_string[i].lower):
              new_m+="   "
              new_m+= m_string[i]
        else:
             new_m+= m_string[i]
    print(m_string)
    print(new_m)

b()
   


