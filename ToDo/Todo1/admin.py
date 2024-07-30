from django.contrib import admin,messages
from django.shortcuts import render,redirect
from .models import ToDo


# Register your models here.
admin.site.register(ToDo)