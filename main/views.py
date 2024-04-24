from django.shortcuts import render
from .forms import SortForm, SearchForm
from .algorithms import insertionSort, bubbleSort, heapSort, mergeSort, quickSort, bucketSort, radixSort, linearSearch, binarySearch

def home(request):
    sortForm = SortForm(request.POST or None)
    searchForm = SearchForm(request.POST or None)
    context = {
        'sortForm' : sortForm,
        'searchForm' : searchForm
    }
    return render(request,'main/home.html',context)


def sort(request):
    searchForm = SearchForm(request.POST or None)
    form = SortForm(request.POST or None)
    if form.is_valid():
        algorithm = form.cleaned_data['algorithm']
        field = form.cleaned_data['field']
        #get data from a particular field and pass it to the function
        #from the results we can then match to see which item represents which record
        if algorithm == 'a':
            items = insertionSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'b':
            items = bubbleSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)     
        elif algorithm == 'c':
            items = heapSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'd':
            items = mergeSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context) 
        elif algorithm == 'e':
            items = quickSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'f':
            items = bucketSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'g':
            items = radixSort()
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)

def search(request):
    form = SearchForm(request.POST or None)
    sortForm = SortForm(request.POST or None)
    if form.is_valid():
        algorithm = form.cleaned_data['algorithm']
        query = form.cleaned_data['query']
        field = form.cleaned_data['field']
        if algorithm == 'a':
            found, index = linearSearch()
            context = {
                'sortForm' : sortForm,
                'searchForm' : form,
                'results' : [found,index]
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