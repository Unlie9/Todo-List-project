from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app.forms import TagForm, TaskForm
from app.models import Task, Tag


class IndexView(ListView):
    model = Task
    template_name = "todo_list/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        tasks = Task.objects.all()

        context['tasks'] = tasks
        return context


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("app:index")


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("app:index")


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "todo_list/delete_task.html"
    success_url = reverse_lazy("app:index")


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


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = True
    task.save()

    return redirect("app:index")


def undo_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = False
    task.save()
    return redirect("app:index")
