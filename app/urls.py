from django.urls import (
    path,
    include
)
from app.views import IndexView, TagListView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("tags/", TagListView.as_view(), name='tags'),
]

app_name = 'app'
