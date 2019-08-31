my_list = ["apple", 5.2, "dog", 8]


def combiner(my_list):
    strlist = ""
    numlist = 0
    for items in my_list:
        if isinstance(items, str):
            strlist += items
        else:
            numlist += items
            
    print(strlist + str(numlist)  )
    return strlist + str(numlist)   
            
combiner(my_list)
    

    
    