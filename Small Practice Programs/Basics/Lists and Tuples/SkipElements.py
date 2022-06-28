# The skip_elements function returns a list containing every 
# other element from an input list, starting with the first element.

def skip_elements(elements):
    new_list = []     
    i = 0

    for index in elements:
        if i%2 == 0:
            new_list.append(elements[i])
        i += 1


    return new_list

print(skip_elements(["a","b","c","d","e","f","g"])) #Should be ['a','c','e','g']
print(skip_elements(['Orange','Pineapple','Strawberry','Kiwi','Peach'])) #Should be ['Orange','Strawberry','Peach']
print(skip_elements([])) #Should be []