from django.urls import path

from . import views

app_name = "quiz1"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("", views.question.as_view(),name= "quiestion"),

]
