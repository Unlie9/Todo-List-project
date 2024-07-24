from django.urls import (
    path,
    include
)
from app.views import IndexView, TagListView, CreateTagView, UpdateTagView, DeleteTagView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("tags/", TagListView.as_view(), name='tags'),
    path("tags/add", CreateTagView.as_view(), name='add-tag'),
    path("tags/<int:pk>/update", UpdateTagView.as_view(), name='update-tag'),
    path("tags/<int:pk>/delete", DeleteTagView.as_view(), name='delete-tag'),
]

app_name = 'app'
