from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image,Student, Staff

# Create your views here.
def login(request):
    if request.method == 'POST' and "student" in request.POST:
        usn = request.POST.get('USN')
        password = request.POST.get('password')
        present = False
        for p in Student.objects.raw("SELECT * FROM myapp_student WHERE USN = '" + usn + "'"):
            present = True
        if present and password == 'student@123':
            return redirect('home')
    elif request.method == 'POST' and "teacher" in request.POST:
        idno = request.POST.get('idno')
        password = request.POST.get('password')
        present = False
        for p in Staff.objects.raw("SELECT * FROM myapp_staff WHERE id = " + idno):
            present = True
        if present and password == 'teacher@123':
            return redirect('achievements')
    return render(request,'login.html')

def menu(request):
    return render(request,'student.html')

def details(request):
    obj = Student.objects.all()
    return render(request,'student_details.html', {'obj':obj})

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'home.html',{'img':img,'form':form})

def logout_request(request):
    return redirect('login')
