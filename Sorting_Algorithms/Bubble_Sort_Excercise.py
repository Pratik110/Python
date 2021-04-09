Link = "https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/2_BubbleSort/bubble_sort_exercise.md"
def bubble_sort(elements,key):
    l = len(elements)
    for i in range(l-1):
        swapped = False
        for j in range(l-1):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break
    return  elements


elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
key = 'name'
print(bubble_sort(elements,key))