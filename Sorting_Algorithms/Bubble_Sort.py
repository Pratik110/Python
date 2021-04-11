def bubble_sort(elements):
    length = len(elements)
    l = len(elements)
    i = 0
    while i < length-1:
        swapped = False
        j = 0
        while j < l-1:
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
            j+=1
        if not swapped:
            break
        l-=1
        i+=1
    return elements

elements = [19,165,12,98,65,49,34,675,616,9,7]
print(bubble_sort(elements))