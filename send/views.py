from django.db import models
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Contact, File
# Create your views here.

class Home(TemplateView):
    template_name = 'send/home.html'

class FileView(ListView):
    model = File
    template_name = 'send/files.html'
    context_object_name = 'files'
    ordering = ['-date']

class UserFileView(ListView):
    model = File
    template_name = 'send/my_files.html'
    context_object_name = 'files'
    ordering = ['-date']

class FileDetail(DetailView):
    model = File

class FileCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = File 
    fields = ['title', 'thumbnail', 'file', 'description', 'option']
    success_message = 'your file has been successfully added'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class FileUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = File 
    fields = ['title', 'thumbnail', 'file', 'description', 'option']
    success_message = 'your file has been successfully updated'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

    def test_func(self):
        file = self.get_object()        
        if self.request.user == file.sender:
            return True
        return False

class ContactForm(FormView):
    models = Contact
    form_class = ''