from django import forms

from store.models import Book

# class BookForm(forms.Form):

#     title=forms.CharField()

#     author=forms.CharField()

#     price=forms.IntegerField()

#     language=forms.CharField()

#     genre=forms.CharField()

#     year=forms.CharField()

#     image=forms.ImageField()

# Model Form
    

class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields ="__all__"

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "author":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "price":forms.NumberInput(attrs={"class":"form-control mb-2"}),
            "language":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "genre":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "year":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "image":forms.FileInput(attrs={"class":"form-control mb-2"}),
        }
