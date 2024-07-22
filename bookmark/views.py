from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import bookmark

class BookmarkLV(ListView):
    model = bookmark

class BookmarkDV(DetailView):
    model = bookmark
