def odd_num(lst):   
    new_list = []
    updated_list = []
    # Multiplies all the values in the list
    for i in lst:
        for x in lst:
            new_list.append(list(i * x for x in lst))
    
    # Joins all of the nested list into one list
    for n in new_list:
        for j in n:
            updated_list.append(j)

    # Determins if there are any odds
    odds = []
    for u in updated_list:
        if u % 2 != 0:
            odds.append(u)
    if len(odds) == 0:
        return False
    else:
        return True
          
print(odd_num([2, 1, 6]))