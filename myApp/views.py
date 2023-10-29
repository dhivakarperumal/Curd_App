from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    students = Student.objects.all() 
    print(students) # Retrieve the students from the database or other data source
    return render(request, 'index.html', {'students': students})

def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")

    
def insert(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'insert.html', {'form': form})

def update(request,pk):
    item = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=item)
    return render(request, 'insert.html', {'form': form})



def delete(request,pk):
    item = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'delete.html', {'item': item})

