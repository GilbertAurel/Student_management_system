from django.shortcuts import render, redirect
from ..students import models as students
from ..classes import models as classes
from ..classroom import models as classroom

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def home_class_view(request, *args, **kwargs):
    return render(request, "homeClass.html", {})


def add_class_view(request, *args, **kwargs):
    if request.method == "POST":
        input_id = request.POST.get("id", None)
        input_name = request.POST.get("name", None)
        classes.Class.objects.create(class_id=input_id, class_name=input_name)
        return redirect("/homeClass")
    return render(request, "addClass.html", {})


def show_class_view(request, *args, **kwargs):
    class_all = classes.Class.objects.all()
    count = classes.Class.objects.all().count()
    return render(request, "showClass.html", {'classes': class_all, 'count': count})


def home_student_view(request, *args, **kwargs):
    return render(request, "homeStudent.html", {})


def add_student_view(request, *args, **kwargs):
    if request.method == "POST":
        input_id = request.POST.get("id", None)
        input_name = request.POST.get("name", None)
        students.Student.objects.create(student_id=input_id, student_name=input_name)
        return redirect("/homeStudent")
    return render(request, "addStudent.html", {})


def show_student_view(request, *args, **kwargs):
    student_all = students.Student.objects.all()
    count = students.Student.objects.all().count()
    return render(request, "showStudent.html", {'students': student_all, 'count': count})


def home_assign_view(request, *args, **kwargs):
    get_class_id = request.GET.get('class')
    get_class_name = classes.Class.objects.filter(class_id=get_class_id)
    get_students = classroom.Classroom.objects.filter(class_id=get_class_id)
    count = classroom.Classroom.objects.filter(class_id=get_class_id).count()
    return render(request, "homeAssign.html", {'student': get_students, 'class': get_class_name, 'count': count, 'class_id': get_class_id})


def add_assign_view(request, *args, **kwargs):
    get_class_id = request.GET.get('class')
    get_class_name = classes.Class.objects.filter(class_id=get_class_id)
    get_students = classroom.Classroom.objects.filter(class_id=get_class_id).values('student_id')
    student_list = students.Student.objects.all()
    count = students.Student.objects.exclude(student_id=[get_students]).count()

    if request.method == "POST":
        input_class_id = request.POST.get("class_id", None)
        input_student_id = request.POST.get("student_id", None)
        classroom.Classroom.objects.create(class_id=input_class_id, student_id=input_student_id)
        return redirect("/homeAssign?class={}".format(input_class_id))

    return render(request, "addToClass.html", {'class': get_class_name, 'student': student_list, 'count': count})