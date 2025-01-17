from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import SignUpForm,SignInForm,ExpenseForm

from django.contrib.auth import authenticate,login,logout

from myapp.models import Expense

from django.db.models import Sum,Count

from django.utils.decorators import method_decorator


from myapp.decorators import signin_required

from django.contrib import messages

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

                messages.success(request,"Login Success")

                return redirect("index")

            else:

                print("======failed======")

                return render(request,"signin.html",{"form":form_instance})

@method_decorator(signin_required,name="dispatch")
class IndexView(View):

    def get(self,request,*args,**kwargs):


        total_expense=Expense.objects.filter(owner=request.user).values("amount").aggregate(total=Sum("amount"))

        print(total_expense)

        category_summary=Expense.objects.filter(owner=request.user).values("category").annotate(total=Sum("amount"),count=Count("category"))

        print(category_summary)

        context={
            "total_expense":total_expense.get("total"),
            "category_summary":category_summary,
           
        }

        return render(request,"index.html",context)

@method_decorator(signin_required,name="dispatch")
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

        
@method_decorator(signin_required,name="dispatch")
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
         
@method_decorator(signin_required,name="dispatch")
class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Expense.objects.get(id=id).delete()

        return redirect("expense-add")

@method_decorator(signin_required,name="dispatch")
class ExpenseUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        expense_object=Expense.objects.get(id=id)

        form_instance =ExpenseForm(instance=expense_object)

        return render(request,"expense_update.html",{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):

         id=kwargs.get("pk")

         expense_object=Expense.objects.get(id=id)

         form_data= request.POST

         form_instance=ExpenseForm(form_data,instance=expense_object)

         if form_instance.is_valid():
             
             form_instance.save()

             return redirect("expense-add")
         
         else:
             
             return render(request,"expense_update.html",{"form":form_instance})
             




