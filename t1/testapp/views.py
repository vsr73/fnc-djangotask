from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def signup(request):
    if request.method=='POST':
        x=request.POST.get("fname")
        y=request.POST.get("lname")
        z=request.POST.get("mobielnum")
        w=request.POST.get("mail")
        t=request.POST.get("addrs")
        p=request.POST.get("pswrd")
        q=request.POST.get("cnfrm_pswrd")
        user=details.objects.filter(mail=w)
        if user:
            messages.error(request,"email already exists try a new mail")
            return redirect('/signup')
        elif p==q:
            try:
                mems=details(fname=x,lname=y,mobile_num=z,address=t,password=p,mail=w)
                mems.save()
                messages.info(request,"login to view details,account created successfully")
                return redirect('/')

            except :
                messages.error(request,'error try again')
                return redirect('/signup')
        else:
            messages.error(request,'password doesnt match')
            return redirect('/signup')


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


def logout(request):
    messages.info(request,"logged out successfully")
    return redirect('/login')
def test(request):
    return redirect('/')
