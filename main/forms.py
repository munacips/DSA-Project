from django import forms
from .models import Student

class SortForm(forms.Form):
    ALGORITHMS = [
        ('a','Insertion sort'),
        ('b','Bubble sort'),
        ('c','Selection sort'),
        ('d','Merge sort'),
        ('e','Quick sort'),
    ]
    FIELDS = []
    for field in Student._meta.get_fields():
        FIELDS.append((field.name,field.name))
    algorithm = forms.ChoiceField(choices=ALGORITHMS,widget=forms.Select(attrs={'placeholder':'Select algorithm'}),label='')
    field = forms.ChoiceField(choices=FIELDS,widget=forms.Select(attrs={'placeholder':'Select field'}),label='')
    descending = forms.BooleanField(required=False)


class SearchForm(forms.Form):
    ALGORITHMS = [
        ('a','Linear Search'),
        ('b','Binary Search'),
        ('c','Ordered Search')
    ]
    FIELDS = []
    for field in Student._meta.get_fields():
        FIELDS.append((field.name,field.name))
    field = forms.ChoiceField(choices=FIELDS,widget=forms.Select(attrs={'placeholder':'Select field'}),label='')
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Search for...'}),label='')
    algorithm = forms.ChoiceField(choices=ALGORITHMS,widget=forms.Select(attrs={'placeholder':'Select algorithm'}),label='')


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','dob','married','bank_balance']