from django.urls import path
from main import views

urlpatterns = [
    path("", views.Index.as_view(), name = "index"),
    #path("question/<int:pk>", views.Question.as_view(), name = 'question')
    path("question/<slug>", views.Question.as_view(), name = 'question')
    
]