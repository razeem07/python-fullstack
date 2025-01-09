from django.shortcuts import render
from django.views.generic import View
from myapp.forms import SignUpForm

# Create your views here.
class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"register.html",{"form":form_instance})