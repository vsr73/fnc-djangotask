from django.shortcuts import render
from .models import *

def signup(request):
    if request.method=='POST':
        x=request.POST.get("fname")
        y=request.POST.get("lname")
        z=request.POST.get("mobielnum")
        w=request.POST.get("mail")
        t=request.POST.get("addrs")
        p=request.POST.get("pswrd")
        q=request.POST.get("cnfrm_pswrd")

        try:
            mems=details(fname=x,lname=y,mobile_num=z,address=t,password=p)
            mems.save()
            return render(request,'testapp/home1.html')
        except:
            return render(request,'testapp/retry.html')
    else:
        return render(request,"testapp/home.html")
def login(request):
    if request.method=='POST':
        email_temp=request.POST.get('mail')
        pswrd_temp=request.POST.get("pswrd")
        check=details.objects.filter(mail=email_temp,password=pswrd_temp).values()
        if check:
            dict={'check':check,}
            return render(request,'testapp/success.html',dict)
        else:
            return render(request,'testapp/invalid.html')
    else:
        return render(request,'testapp/login.html')



def mainpage(request):
    return render(request,'testapp/mainpage.html')
