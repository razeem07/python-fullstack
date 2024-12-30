from django import forms

class BookForm(forms.Form):

    title=forms.CharField()

    author=forms.CharField()

    price=forms.IntegerField()

    language=forms.CharField()

    genre=forms.CharField()

    year=forms.CharField()
    