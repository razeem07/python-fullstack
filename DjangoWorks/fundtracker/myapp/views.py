from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import SignUpForm,SignInForm,ExpenseForm

from django.contrib.auth import authenticate,login,logout

from myapp.models import Expense

# Create your views here.
class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"register.html",{"form":form_instance})
    
    def  post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance = SignUpForm(form_data)

        if form_instance.is_valid():

            form_instance.save()

            print("===account created")

            return redirect("register")
        
        else:

            print("===failed====")

            return render(request,"register.html",{"form":form_instance})
        

class SignInView(View):
    
    def get(self,request,*args,**kwargs):

        form_instance = SignInForm()

        return render(request,"signin.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance = SignInForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_instance = authenticate(request,username=uname,password=pwd)

            if user_instance:

                login(request,user_instance)

                print("===Success==")

                return redirect("index")

            else:

                print("======failed======")

                return render(request,"signin.html",{"form":form_instance})


class IndexView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"index.html")


class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

        

class ExpenseView(View):

     def get(self,request,*args,**kwargs):

        form_instance = ExpenseForm()

        qs=Expense.objects.filter(owner=request.user).order_by("-created_at")

        return render(request,"expense_add.html",{"form":form_instance,"data":qs})
     
     
     def post(self,request,*args,**kwargs):
         
         form_data=request.POST

         form_instance=ExpenseForm(form_data)

         if form_instance.is_valid():
             
             form_instance.instance.owner=request.user
             
             form_instance.save()

             return redirect("expense-add")
         
         else:
             
             return render(request,"expense_add.html",{"form":form_instance})
         

class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Expense.objects.get(id=id).delete()

        return redirect("expense-add")