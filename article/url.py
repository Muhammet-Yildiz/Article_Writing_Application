from django.contrib import admin
from django.urls import path

from . import views 


app_name ="article"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('',views.articles,name="articles"),
    path('addComment/<int:id>',views.addComment,name="comment"),
    path('answer/<int:id>',views.addAnswer,name="answer"),

    path('commentLike/<int:id>',views.addCommentLike,name="commentLike"),
    path('commentdisLike/<int:id>',views.commentdisLike,name="commentdisLike"),

    path('addAnswerLike/<int:id>',views.addAnswerLike,name="addAnswerLike"),
    path('addAnswerdisLike/<int:id>',views.addAnswerdisLike,name="addAnswerdisLike"),


]

