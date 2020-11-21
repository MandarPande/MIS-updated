from django.shortcuts import render
from .forms import ImageForm
from .models import Image,Student

# Create your views here.
def login(request):
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
