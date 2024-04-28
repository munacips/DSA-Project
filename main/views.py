from django.shortcuts import render
from .forms import SortForm, SearchForm, AddStudentForm
from .algorithms import insertionSort, bubbleSort, orderedSearch, selectionSort, mergeSort, quickSort, linearSearch, binarySearch
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
            if form.cleaned_data['descending']:
                items = items[::-1]
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'b': # done
            items = bubbleSort(field)
            if form.cleaned_data['descending']:
                items = items[::-1]
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)     
        elif algorithm == 'c': #done
            items = selectionSort(field)
            if form.cleaned_data['descending']:
                items = items[::-1]
            context = {
                'sortForm' : form,
                'searchForm' : searchForm,
                'items' : items
            }
            return render(request,'main/home.html',context)
        elif algorithm == 'd': # done
            students = Student.objects.all()
            elements = list(students)
            items = mergeSort(field)
            if form.cleaned_data['descending']:
                items = items[::-1]
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
            if form.cleaned_data['descending']:
                items = items[::-1]
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
            found, element, index = linearSearch(query,field)
            context = {
                'sortForm' : sortForm,
                'searchForm' : form,
                'found' : found,
                'element' : element,
                'results' : True,
                'index' : index
            }
            return render(request,'main/home.html',context)
        if algorithm == 'b':
            found, element, index = binarySearch(query,field)
            context = {
                'sortForm' : sortForm,
                'searchForm' : form,
                'found' : found,
                'element' : element,
                'results' : True,
                'index' : index
            }
            return render(request,'main/home.html',context)
        if algorithm == 'c':
            found, element, index = orderedSearch(query,field)
            context = {
                'sortForm' : sortForm,
                'searchForm' : form,
                'found' : found,
                'element' : element,
                'results' : True,
                'index' : index
            }
            return render(request,'main/home.html',context)
        

def addstudent(request):
    form = AddStudentForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        dob = form.cleaned_data['dob']
        married = form.cleaned_data['married']
        bank_balance = form.cleaned_data['bank_balance']
        new_student, created = Student.objects.get_or_create(first_name=first_name,last_name=last_name,email=email,dob=dob,married=married,bank_balance=bank_balance)
        if created:
            new_student.save() #redundant
            sortForm = SortForm()
            searchForm = SearchForm()
            context = {
                'sortForm' : sortForm,
                'searchForm' : searchForm
            }
            return render(request,'main/home.html',context)
    context = {
        'form' : form
    }
    return render(request,'main/add_students.html',context)
