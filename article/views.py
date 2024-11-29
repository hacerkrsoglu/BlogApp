from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article ,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html",{"articles":articles})
    
    
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})


def index(request):
    #return HttpResponse("<h3>Anasayfa</h3>")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

#def detail(request,id):
#    return HttpResponse("Detail:"+ str(id))
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html",context)

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
#articlearın commentlerine modelde tanımladığımız related name alanını kullanarak ulaşabilirim
    comments = article.comments.all()

    return render( request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id=id)#nesne varsa nesneyi döndürür yani o id de var mı diye kontol ediyoruz
    form = ArticleForm(request.POST or None , request.FILES or None,instance=article)#article nesnesiyle doldurulur
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):

    article = get_object_or_404(Article, id=id)#başa hangi modelden almak istediğimizi yazarız

    article.delete()
    messages.success(request,"Makale Başarıyla Silindi.")
    return redirect("article:dashboard")#article uygulaması altındaki dashboarda git



def addComment(request, id):
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article= article
        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id":id}))#reverse fonk kulanacaz

        
