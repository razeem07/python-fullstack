from django.shortcuts import render

from django.views.generic import View

# Create your views here.

class HelloWorldView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"helloworld.html")
    

class GoodMorningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"goodmorning.html")
    

class GoodAfternoonView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"goodafternoon.html")
    

    
class GoodEveningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"goodevening.html")

    
class SachinView(View):

    def get(self,request,*args,**kwargs):

        data={
            "name":"sachin",
             "age":55,
             "odi":300,
             "test":200
        }
        return render(request,"sachin.html",data)

class MohanlalView(View):

    def get(self,request,*args,**kwargs):

        data={
            "name":"Mohanlal",
            "movies":300,
            "language":"Malayalam"
        }

        return render(request,"mohanlal.html",data)
