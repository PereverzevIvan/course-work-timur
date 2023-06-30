from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def error_404(request, exception):
    data = {
        'exception': exception
    }
    return render(request,'404.html', data)

def show_all_news(request, page_no:int):
    news = list(Article.objects.all()) * 100
    return render(request, 'all_news.html', {'news': news})

def show_one_article(request, article_id:int):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article_id)

    return render(request, 'one_article.html', {'article': article, 'comments': comments})

def add_comment(request, article_id:int):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated and get_object_or_404(Article, pk=article_id):
            comment = Comment()
            comment.article_id = article_id
            comment.author_id = user.id
            comment.text = request.POST.get('comment-text')
            comment.save()
            return HttpResponsePermanentRedirect(reverse('mainApp:one_article', kwargs={'article_id': article_id}))
        else:
            return render(request, 'error.html', {'error_title': 'Ошибка добавления', 
                                                  'error_text': 'Не удалось добавить комментарий'})
        

def delete_comment(request, comment_id:int):
    comment = get_object_or_404(Comment, pk=comment_id)
    article_id = comment.article_id
    user = request.user

    if user.is_authenticated and comment.author_id == user.id:
        comment.delete()
        return HttpResponsePermanentRedirect(reverse('mainApp:one_article', kwargs={'article_id': article_id}))
    return render(request, 'error.html', {'error_title': 'Ошибка удаления', 
                                                  'error_text': 'Вы не можете удалить комментарий другого человека'})