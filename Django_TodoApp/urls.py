from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='todo_url'),
    path('ofv/', views.TodoFormView, name='todo_url'),
    path('sv/', views.showView, name='show'),
    path('up/<int:currentId>', views.updateView, name='update'),
    path('del/<int:currentId>', views.deleteView, name='delete'),
]