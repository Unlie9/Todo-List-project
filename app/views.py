from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.forms import TagForm
from app.models import Task, Tag


class IndexView(ListView):
    model = Task
    template_name = "todo_list/index.html"


class TagListView(ListView):
    model = Tag
    template_name = "todo_list/tag.html"

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)

        tags = Tag.objects.all()
        context["tags"] = tags

        return context


class CreateTagView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("app:tags")


class UpdateTagView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("app:tags")


class DeleteTagView(DeleteView):
    model = Tag
    template_name = "todo_list/delete_tag.html"
    success_url = reverse_lazy("app:tags")

