"""
URL configuration for BookCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/add/",views.BookCreateView.as_view(),name="add"),
    path("books/all/",views.BookListView.as_view(),name="book-all"),
    path("books/<int:pk>/",views.BookDetailView.as_view(),name="book-detail"),
    path("books/<int:pk>/remove/",views.BookDeleteView.as_view(),name="book-delete"),
    path("books/<int:pk>/change/",views.BookUpdateView.as_view(),name="book-update"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
