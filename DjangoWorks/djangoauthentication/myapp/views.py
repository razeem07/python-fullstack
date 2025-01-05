from django.shortcuts import render,redirect
from django.views.generic import View

from myapp.forms import SignUpForm,SignInForm
from django.contrib.auth.models import User

# Create your views here.

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"signup.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignUpForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            print("=====account created=====")

            return redirect("signin")
        
        print("==failed===")

        return render(request,"signup.html",{"form":form_instance})

            

class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignInForm()

        return render(request,"signin.html",{"form":form_instance})
    

