# Speical Values for Rendering & HTTP
from django.shortcuts import render

# Import Models
from .models import TaskModel

# This enables us the API VIEW 
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Form Editing for MODELS
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

# TEST API VIEWwewrwesadasdasdasdkooooo

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# import local data 
from .serializers import TaskModelSerializer 
from .models import TaskModel 

class hAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
    
# create a viewset 
class TaskViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = TaskModel.objects.all() 
      
    # specify serializer to be used 
    serializer_class = TaskModelSerializer 
    
    


# class AuthorCreateView(CreateView):
#     model = Author
#     fields = ["name"]


# class AuthorUpdateView(UpdateView):
#     model = Author
#     fields = ["name"]


# class AuthorDeleteView(DeleteView):
#     model = Author
#     success_url = reverse_lazy("author-list")





from django.core.mail import send_mail
def NewTaskView(CreateView, form):
    model = TaskModel
    fields = "__all__"
    
    if form.is_valid():
        subject = form.cleaned_data["title"]
        message = form.cleaned_data["description"]
        sender = form.cleaned_data["created_by"]
        cc_myself = form.cleaned_data["assigned_by"]

        recipients = ["info@example.com"]
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect("/thanks/")