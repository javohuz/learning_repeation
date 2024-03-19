from django.urls import path
from .views import TodoApiView , DetailApiTodo

urlpatterns = [
    path('<int:pk>/', DetailApiTodo.as_view() ),
    path('' , TodoApiView.as_view())
]