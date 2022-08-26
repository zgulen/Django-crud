from unicodedata import name
from django.urls import path
from .views import student_add, student_delete, student_detail, student_list, student_update, team

urlpatterns = [
    path('', team, name='team'),
    path("list/", student_list, name='students'),
    path('add/', student_add, name='add'),
    path('update/<int:id>', student_update, name='update'),
    path('delete/<int:id>', student_delete, name='delete'),
    path('detail/<int:id>', student_detail, name='detail'),
]
