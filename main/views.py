from django.shortcuts import render
from .forms import SortForm, SearchForm
from .algorithms import insertionSort, bubbleSort, selectionSort, mergeSort, quickSort, linearSearch, binarySearch
from .models import Student

def home(request):
    sortForm = SortForm(request.POST or None)
    searchForm = SearchForm(request.POST or None)
    context = {
        'sortForm' : sortForm,
        'searchForm' : searchForm
    }
    return render(request,'main/home.html',context)


def sort(request):
    searchForm = SearchForm()
    form = SortForm(request.POST or None)
    if form.is_valid():
        algorithm = form.cleaned_data['algorithm']
        field = form.cleaned_data['field']
        #get data from a particular field and pass it to the function
        #from the results we can then match to see which item represents which record
        if algorithm == 'a': # done
            items = insertionSort(field)
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'b': # done
            items = bubbleSort(field)
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)     
        elif algorithm == 'c': #done
            items = selectionSort(field)
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'd': # done
            students = Student.objects.all()
            elements = list(students)
            items = mergeSort(elements,field)
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context) 
        elif algorithm == 'e': #done
            students = Student.objects.all()
            elements = list(students)
            start = 0
            end = len(elements) -1
            items = quickSort(elements,start,end,field)
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)

def search(request):
    form = SearchForm(request.POST or None)
    sortForm = SortForm()
    if form.is_valid():
        algorithm = form.cleaned_data['algorithm']
        query = form.cleaned_data['query']
        field = form.cleaned_data['field']
        if algorithm == 'a':
            found, element = linearSearch(query,field)
            context = {
                'sortForm' : sortForm,
                'searchForm' : form,
                'found' : found,
                'element' : element,
                'results' : True
            }
            return render(request,'main/home.html',context)
        if algorithm == 'b':
            found, index = binarySearch()
            context = {
                'sortForm' : sortForm,
                'searchForm' : form,
                'results' : [found,index]
            }
            return render(request,'main/home.html',context)