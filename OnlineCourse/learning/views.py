from django.contrib.auth import authenticate,login,logout
from .forms import StudentForm
from django.shortcuts import render,redirect
from .models import Course, Marks


def showindex(request):
    return render(request,'index.html')
def showcourses(request):
    rows=Course.objects.all()
    return render(request,'courses.html',{'values':rows})
def showsignup(request):
    if request.POST:
        frm=StudentForm(request.POST,request.FILES)
        frm.save()
        return redirect('/login')
    frm=StudentForm()
    return render(request,'signup.html',{'myform':frm})
def showlogin(request):
    if request.POST:
        uname=request.POST['username']
        pword=request.POST['password']
        user=authenticate(username=uname,password=pword)
        if user is None:
            return redirect("/")
        else:
            return redirect('/welcome')
    return render(request,'login.html')
def showwelcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request, 'home.html')

def readmarks(request):
    rno = request.GET.get('rollno')
    if not rno:
        return render(request, 'home.html')

    try:
        row = Marks.objects.get(rollnumber=rno)
    except Marks.DoesNotExist:
        return render(request, 'home.html', {'error_message': 'Student not found'})

    row.passed_c = row.c >= 35
    row.passed_python = row.python >= 35
    row.passed_java = row.java >= 35
    row.passed_react = row.react >= 35
    row.passed_django = row.django >= 35

    row.passed = all([
        row.passed_c,
        row.passed_python,
        row.passed_java,
        row.passed_react,
        row.passed_django,
    ])
    row.total = row.c + row.python + row.java + row.react + row.django
    row.save()

    return render(request, 'home.html', {'values': row})

    
# Create your views here.

