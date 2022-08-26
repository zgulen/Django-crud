import re
from django.shortcuts import render,redirect
from me04.models import Student
from.forms import StudentForm

# Create your views here.
def team(request):
    return render(request, 'me04/index.html')

def student_list(request):
    students = Student.objects.all()
    context = {
        'student': students
    }
    return render(request, 'me04/student_list.html', context)


def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/list/')
    context = {
        'form': form
    }
    return render(request, 'me04/student_add.html', context)

def student_update(request, id):
    student=Student.objects.get(id = id)
    form = StudentForm(instance=student)
    if request.method =='POST':
        form= StudentForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect('/list/')
    context={
        'form':form
    }
    return render(request, 'me04/student_update.html', context)

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('/list/')
    context = {
            'student':student
        }
    return render(request, 'me04/student_delete.html',context)

def student_detail(request, id):        
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'me04/student_detail.html', context)