from django.shortcuts import render,redirect

from django.views.generic import View

from store.forms import BookForm

from store.models import Book



# Create your views here.


class BookCreateView(View):

    def get(self, request,*args,**kwargs):

        form_instance=BookForm()

        return render(request,"book_create.html",{"form":form_instance})
        


    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BookForm(form_data)

        if form_instance.is_valid():
            
            data=form_instance.cleaned_data

            Book.objects.create(
                title=data.get("title"),
                author=data.get("author"),
                price=data.get("price"),
                language=data.get("language"),
                genre=data.get("genre"),
                year= data.get("year")

            )

            return redirect("book-all")

        return render(request,"book_create.html",{"form":form_instance})



class BookListView(View):

    def get(self,request,*args,**kwargs):

        qs=Book.objects.all()
        
        return render(request,"book_list.html",{"data":qs})
    

class BookDetailView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs=Book.objects.get(id=id)

        return render(request,"book_detail.html",{"data":qs})
    

class BookDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Book.objects.get(id=id).delete()

        return redirect("book-all")
    
    
class BookUpdateView(View):

    def get(self,request,*args,**kwargs):

        id =kwargs.get("pk")

        book_obj=Book.objects.get(id=id)

        book_dictionary={
           
            "title":book_obj.title,
             "author":book_obj.author,
             "price":book_obj.price,
             "language":book_obj.language,
             "genre":book_obj.genre,
             "year":book_obj.year
        }



        form_instance=BookForm(initial=book_dictionary)

        return render(request,"book_update.html",{"form":form_instance})

    
    def post(self,request,*args,**kwargs):

        id =kwargs.get("pk")

        form_data=request.POST

        form_instance=BookForm(form_data)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            Book.objects.filter(id=id).update(**data)

            return redirect("book-all")
        
        return render(request,"book_update.html",{"form":form_instance})
        
     



