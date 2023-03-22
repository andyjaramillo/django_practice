from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    #all these urls will be added
    #after the smart url
   path('notes', views.NotesListView.as_view(), name="notes.list"),
   path('notes/<int:pk>' , views.NotesDetailView.as_view(), name="notes.detail"),
   path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),

]