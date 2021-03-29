from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student


# Create your views here.

# insert into database
def create(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return student_list(request)
    else:
        fm = StudentRegistration()

    diction = {"form": fm}
    return render(request, 'create.html', context=diction)


# show view hear
def student_list(request):
    stud = Student.objects.all()
    diction = {"stud": stud}
    return render(request, 'show.html', context=diction)


# update data
def update(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return student_list(request)
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    diction = {"form": fm}
    return render(request, 'update.html', context=diction)


# delete view her

def delete_data(request, id):
    if request.method == "POST":
        dl = Student.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')