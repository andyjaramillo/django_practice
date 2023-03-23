from django.shortcuts import render
from .models import Notes
from django.http import Http404
from .forms import NotesForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"
    template_name = "notes/notes_delete.html"
# Create your views here.
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
     model = Notes
     context_object_name = "notes"
     template_name = "notes/notes_list.html"
     #if not logged in, will be directed to the admin link
     login_url = "/admin"
     #display only the notes gotton by that user
     def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
     model = Notes
     context_object_name = "note"
     template_name = "notes/notes_detail.html"