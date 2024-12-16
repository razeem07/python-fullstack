from django.shortcuts import render

from django.views.generic import View

from  operation.forms import BmiForm,VehicleForm,BmrForm,MilegeForm



# Create your views here.

class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1= form_data.get("num1")

        num2= form_data.get("num2")

        result = int(num1)+int(num2)

        print(f" Result ",result)

        data={"output":result}

        return render(request,"add.html",data)


class SubtractionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"sub.html")
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1= form_data.get("num1")

        num2= form_data.get("num2")

        result = int(num1)-int(num2)

        print(f" Result ",result)

        data={"output":result}

        return render(request,"sub.html",data)


class BmiView(View):
    def get(self,request,*args,**kwargs):

        form_instance= BmiForm()

        context={"form":form_instance}

        return render(request,"bmi.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance=BmiForm(form_data)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            height=data.get("height")

            weight=data.get("weight")

            bmi = weight/(height/100)**2

            print(bmi)

            return render(request,"bmi.html",{"form":form_instance,"result":bmi})




class VehicleAddView(View):
     
    def get(self,request,*args,**kwargs):

        form_instance= VehicleForm()

        context={"form":form_instance}

        return render(request,"bmi.html",context)



class BmrView(View):
    def get(self,request,*args,**kwargs):

        form_instance= BmrForm()

        context={"form":form_instance}

        return render(request,"bmr.html",context)
    

class MilegeView(View):

    def get(self,request,*args,**kwargs):

        form_instance= MilegeForm()

        context={"form":form_instance}

        return render(request,"milage.html",context)
    

    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance=MilegeForm(form_data)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            distance=data.get("distance")

            consumption=data.get("consumption")

            MILAGE = distance/consumption

            print(MILAGE)

            return render(request,"bmi.html",{"form":form_instance,"result":MILAGE})


