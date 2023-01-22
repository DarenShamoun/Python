# the skip_elements function to return every other 
# element from the list, this time using the enumerate 
# function to check if an element is on an even position or an odd position.

def skip_elements(elements):
    even_elements = []
    for index, item in enumerate(elements):
        if index % 2 == 0:
            even_elements.append(item)
    return even_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']