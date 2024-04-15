from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Name

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    sobj=Name.objects.all()
    return render(request,"index.html",{'result':obj,'res':sobj})
#def addition(request):
    #x=int(request.GET["num1"])
    #y=int(request.GET["num2"])
    #res=x+y
    #res1=x-y
    #res2=x*y
    #res3=x/y
    #return render(request,"result.html")
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse('hii contact')

