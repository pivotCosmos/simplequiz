from django.urls import path
from . import views

# URL Config
urlpatterns = [
    path('hello/', views.say_hello),
    path('manager/set_quiz', views.manager_quiz_view),
    path('submit/', views.insert_single, name='insert-single-quiz'),
]