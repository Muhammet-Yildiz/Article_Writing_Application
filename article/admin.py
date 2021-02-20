from django.contrib import admin

from .models import Article,Comment,Answer

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title","author","created_date"]
    list_display_links =["title","created_date"]
    list_filter = ["created_date"]
    class Meta :
         model = Article
          

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ["comment_content"]
    list_display = ["comment_content","comment_author","comment_date"]
    list_display_links =["comment_content","comment_date"]
    list_filter = ["comment_date"]
    class Meta :
         model = Comment



@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ["answer_content"]
    list_display = ["answer_content","answer_author","answer_date"]
    list_display_links =["answer_content","answer_date"]
    list_filter = ["answer_date"]
    class Meta :
         model = Answer

