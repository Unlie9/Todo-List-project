from django.urls import (
    path,
)
from app.views import IndexView, TagListView, CreateTagView, UpdateTagView, DeleteTagView, CreateTaskView, \
    UpdateTaskView, DeleteTaskView, complete_task, undo_task

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add_task/", CreateTaskView.as_view(), name='add-task'),
    path("update_task/<int:pk>/", UpdateTaskView.as_view(), name='update-task'),
    path("delete_task/<int:pk>/", DeleteTaskView.as_view(), name='delete-task'),
    path("complete_task/<int:task_id>/", complete_task, name='complete-task'),
    path("undo_task/<int:task_id>/", undo_task, name='undo-task'),
    path("tags/", TagListView.as_view(), name='tags'),
    path("tags/add", CreateTagView.as_view(), name='add-tag'),
    path("tags/<int:pk>/update", UpdateTagView.as_view(), name='update-tag'),
    path("tags/<int:pk>/delete", DeleteTagView.as_view(), name='delete-tag'),
]

app_name = 'app'
