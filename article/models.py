from django.db import models
from user.models import Profile 
from ckeditor.fields import RichTextField
from django.views.generic import ListView
class Article(models.Model) :

    author =models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name='Yazar')
    title = models.CharField(max_length=50,verbose_name='Başlık')
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    article_image = models.FileField(blank =True , null = True ,verbose_name = "Makaleye Fotograf yükleyin " )
    def __str__(self):
        return self.title

    class Meta :
        ordering =['-created_date']


    

class Comment(models.Model) :
    article = models.ForeignKey(Article , on_delete = models.CASCADE ,verbose_name="Makalemiz ",related_name="commentss" )
    comment_author = models.ForeignKey("auth.User",verbose_name="Yorum yazarı ",on_delete = models.CASCADE)
    comment_content = models.CharField(max_length=100 , verbose_name="Yorum ")
    comment_date = models.DateTimeField(auto_now_add=True )
    likes = models.ManyToManyField("auth.User",related_name="Related_comment_like")
    dislikes = models.ManyToManyField("auth.User",related_name="Related_comment_dislike")
    def total_likes(self):
        return self.likes.count()
    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.comment_content 


    class Meta : 
        ordering =['-comment_date']

    
class Answer(models.Model) :
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,verbose_name="Yorum" ,related_name="answerr")
    answer_author = models.ForeignKey("auth.User" ,on_delete =models.CASCADE,verbose_name="cevap yazarı ")
    answer_content  = models.CharField( max_length=100 , verbose_name="Cevap")
    answer_date = models.DateTimeField(auto_now_add=True  )
    likess = models.ManyToManyField("auth.User",related_name="answer_likes")
    dislikess = models.ManyToManyField("auth.User",related_name="answer_dislikes")
    def total_likess(self):
        return self.likess.count()
    def total_dislikess(self):
        return self.dislikess.count()
    
    def __str__(self ):
        return self.answer_content

    class Meta : 
        ordering =['answer_date']