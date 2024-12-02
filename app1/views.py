from django.shortcuts import render

# Create your views here.
def pen(request):
    return render(request,'pen.html')