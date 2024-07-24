from django.shortcuts import render
from django.views.generic import ListView

from app.models import Task, Tag


class IndexView(ListView):
    model = Task
    template_name = "todo_list/index.html"


class TagListView(ListView):
    model = Tag
    template_name = "todo_list/tag.html"

