def bubble_sort(elements):
    length = len(elements)
    j = 0
    while j < length-1:
        i = 0
        while i < length-1:
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] =  elements[i+1]
                elements[i+1] = temp
            i+=1
        j+=1
    return elements

elements = [19,165,12,98,65,49,34,675]
print(bubble_sort(elements))