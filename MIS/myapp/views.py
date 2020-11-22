from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image,Student

# Create your views here.
def login(request):
    if request.method == 'POST' :
        usn = request.POST.get('USN')
        password = request.POST.get('password')
        present = False
        for p in Student.objects.raw("SELECT * FROM myapp_student WHERE USN = '" + usn + "'"):
            present = True
        if present and password == 'student@123':
            return redirect('home')
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
