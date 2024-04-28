from .models import Student


def insertionSort(field):
    students = Student.objects.all()
    elements = list(students)
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and getattr(anchor,field) < getattr(elements[j],field):
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
    return elements

def bubbleSort(field):
    students = Student.objects.all()
    elements = list(students)
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if getattr(elements[j],field) > getattr(elements[j+1],field):
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break
    return elements

def selectionSort(field):
    students = Student.objects.all()
    elements = list(students)
    size_of_list = len(elements)

    for i in range(size_of_list):
        for j in range(i+1, size_of_list):

            if getattr(elements[j],field) < getattr(elements[i],field):
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
    return elements

def mergeSort(elements,field):
    f = field
    if len(elements) <= 1:
        return elements

    mid = len(elements)//2

    left = elements[:mid]
    right = elements[mid:]

    left = mergeSort(left,field)
    right = mergeSort(right,field)

    return merge_two_sorted_lists(left, right, f)

def merge_two_sorted_lists(a,b,field):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if getattr(a[i],field) <= getattr(b[j],field):
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

def quickSort(elements,start,end,field):
    if start < end:
        pi = partition(elements, start, end,field)
        quickSort(elements, start, pi-1,field)
        quickSort(elements, pi+1, end,field)
    else:
        pass
    return elements

def partition(elements, start, end,field):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and getattr(elements[start],field) <= getattr(pivot,field):
            start+=1

        while getattr(elements[end],field) > getattr(pivot,field):
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def linearSearch(query,field):
    students = Student.objects.all()
    elements = list(students)
    for element in elements:
        if str(getattr(element,field)) == str(query):
            return True, element, elements.index(element)
    return False, 0, 0

def binarySearch(query,field):
    students = Student.objects.all().order_by(field)
    elements = list(students)
    size_of_list = len(elements) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list
    found = False

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2

        if str(getattr(elements[mid_point],field)) == query:
            found = True
            return found, elements[mid_point], mid_point

        if query > str(getattr(elements[mid_point],field)):
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
    if not found:
        return found, 0, 0
    
def orderedSearch(query,field):
    students = Student.objects.all().order_by(field)
    elements = list(students)
    elements_size = len(elements)
    for i in range(elements_size):
        if query == str(getattr(elements[i],field)):
            return True, elements[i], i
        elif str(getattr(elements[i],field)) > query:
            return False, 0, 0