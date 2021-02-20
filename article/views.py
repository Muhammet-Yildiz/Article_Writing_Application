from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from .models import Article,Comment,Answer
from  .forms import ArticlesForm
from django.contrib.auth.models import User

from django.core.paginator import Paginator,EmptyPage

from django.contrib.auth.decorators import login_required
import requests


from django.http import JsonResponse

def index(request) :
    return render(request,"index.html")


def about(request) :
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request) :
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" :articles
    }
    return render(request,"dashboard.html",context )



def articles(request) :
    keyword = request.GET.get("query")
    if keyword :

        all_articles = Article.objects.filter(title__contains =keyword)

    else :
        all_articles = Article.objects.all()

    p = Paginator(all_articles, 4)

    page_num = request.GET.get("page",1)


    try : 
        sayfa = p.page(page_num)

    except EmptyPage : 

        sayfa = p.page(1)

    context ={
        "all_articles" :sayfa ,
        "page_range":p.page_range,
        "sayfa_sayısı":p.num_pages,
        "keyword":keyword
    }
    return render(request,"articles.html",context)


@login_required(login_url="user:login")
def addarticle(request) :
    form = ArticlesForm(request.POST or None ,request.FILES or None ) 

    if form.is_valid() :
        
        clientkey = request.POST['g-recaptcha-response']

        secretkey = '6Ld_d1kaAAAAADl_A50ezq3qr7fO6dnt0avL-X4J'

        capthchaData ={
            'secret' :secretkey ,
            'response':clientkey

        }
        
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=capthchaData)
        
        
        response = r.json()
        
        
        verify = response["success"]
        
        
        if verify : 
            article = form.save(commit=False)   

            article.author =request.user
            article.save()

            messages.success(request,"Makaleniz basarıyla kaydedildi ")
            return redirect("index")

        else :
            messages.info(request, 'reCAPTCHA onaylanmadı . Makalenizi yazdıktan sonra onaylayınız  .')

            return redirect("article:addarticle")

    else :
        return render(request,"addarticle.html",{"form" :form })




@login_required(login_url="user:login")
def detail(request ,id ): 

    article = get_object_or_404(Article , id =id )

    comments = article.commentss.all()

    return render(request , "detail.html",{"article" : article ,"comments":comments })




    
@login_required(login_url="user:login")
def updateArticle(request,id) :
    article = get_object_or_404(Article, id =id )

    if (article.author != request.user) :
        messages.info(request,"Makaleyi guncelleme yetkiniz yok ") 
        return redirect("index")
    
    
    form =ArticlesForm(request.POST or None , request.FILES or None  ,instance=article )
    
    if form.is_valid() :
        article = form.save(commit=False )

        article.author = request.user

        article.save()
        messages.success(request,"Makaleniz basarıyla guncellendi ")
        return redirect("index")
    
    else :
        return render(request ,"update.html",{"form":form })

@login_required(login_url="user:login")
def deleteArticle(request ,id ) : 

    article = get_object_or_404(Article, id= id )
    if( article.author != request.user):
        messages.info(request, "Bu makaleyi silme yetkiniz yok ")
        return redirect("index")
   
    article.delete()

    messages.success(request, "Makaleniz basarıyla silindi ")
    return redirect("article:dashboard")


@login_required(login_url="user:login")
def addComment(request ,id ): 
    
    article = get_object_or_404(Article, id =id )   

    if request.method =="POST" :
        comment_author =request.user 

        comment_content =request.POST["içerik"]

        newComment = Comment(comment_author =comment_author , comment_content = comment_content)
        newComment.article = article

        newComment.save()
    
    return JsonResponse({"bool" :True ,"commentid": int(newComment.id),"commentlike":newComment.likes.count() ,"commentdislike":newComment.dislikes.count() })

@login_required(login_url="user:login")
def addAnswer(request,id ):
    comment = get_object_or_404(Comment, id =id )  
    
    
    if request.method =="POST":
        answer_author =request.user
        answer_content = request.POST.get("answer_content")
        newAnswer = Answer(answer_author =answer_author , answer_content =answer_content)
        newAnswer.comment = comment
        id = comment.article_id 
        newAnswer.save()
    return redirect("/articles/article/"+ str(id))


def addCommentLike(request,id ) : 
    comment = get_object_or_404(Comment,id =id )

    if not(comment.likes.filter(id =request.user.id).exists()) : 

        if comment.dislikes.filter(id =request.user.id).exists():
            comment.likes.add(request.user)
            comment.dislikes.remove(request.user)
        else : 
            comment.likes.add(request.user)
    else : 
        comment.likes.remove(request.user) 

    data = {
        "likesayı":comment.likes.count(),
        "dislikesayı":comment.dislikes.count()
    }
    return JsonResponse(data)

def commentdisLike(request,id ) : 

    comment = get_object_or_404(Comment,id=id)
    if not(comment.dislikes.filter(id =request.user.id).exists()):
    
        if comment.likes.filter(id =request.user.id).exists():
            comment.likes.remove(request.user)
            comment.dislikes.add(request.user) 
        else :
            comment.dislikes.add(request.user) 
    
    else : 
        comment.dislikes.remove(request.user) 

    data = {
        "likesayı":comment.likes.count(),
        "dislikesayı":comment.dislikes.count()

    }
    return JsonResponse(data)



def addAnswerLike(request,id):
    answer = get_object_or_404(Answer,id=id)

    if not(answer.likess.filter(id =request.user.id).exists()):
        if answer.dislikess.filter(id =request.user.id).exists():
            answer.likess.add(request.user)
            answer.dislikess.remove(request.user)
        else : 
            answer.likess.add(request.user)

    else : 
        answer.likess.remove(request.user) 


    data = {
        "answerlikesayısı":answer.likess.count() ,
        "answerdislikesayısı":answer.dislikess.count()

    }
    return JsonResponse(data)


def addAnswerdisLike(request,id):
    answer = get_object_or_404(Answer,id=id)

    if not(answer.dislikess.filter(id =request.user.id).exists()):
        if answer.likess.filter(id =request.user.id).exists():
            answer.likess.remove(request.user)
            answer.dislikess.add(request.user)
        else : 
            answer.dislikess.add(request.user)

    else : 
        answer.dislikess.remove(request.user)
    

    data = {
        "answerlikesayısı":answer.likess.count() ,
        "answerdislikesayısı":answer.dislikess.count()

    }

    return JsonResponse(data)


