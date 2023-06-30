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

def show_all_news(request):
    news = list(Article.objects.all())[::-1]
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


def show_all_advertisements(request):
    advertisements = list(Advertisement.objects.all())[::-1]

    return render(request, 'all_advertisements.html', {'advertisements': advertisements})

def show_one_advertisement(request, advertisement_id):
    advertisement = get_object_or_404(Advertisement, pk=advertisement_id)
    car = get_object_or_404(Car, advertisement_id=advertisement_id)

    return render(request, 'one_advertisement.html', {'advertisement': advertisement, 'car': car})

def add_advertisement(request):
    if request.method == 'GET':
        return render(request, 'add_advertisement.html')
    elif request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        text = request.POST.get('text')
        price = request.POST.get('price')
        image = request.FILES['image']
        mark = request.POST.get('mark')
        model = request.POST.get('model')
        year = request.POST.get('year')
        color = request.POST.get('color')
        vin = request.POST.get('vin')
        
        new_advertisement = Advertisement()
        new_advertisement.author_id = user.id
        new_advertisement.image = image
        new_advertisement.title = title
        new_advertisement.text = text
        new_advertisement.price = price
        new_advertisement.is_close = False

        new_advertisement.save()

        new_car = Car()
        new_car.mark = mark
        new_car.model = model
        new_car.year = year
        new_car.color = color
        new_car.vin_number = vin
        new_car.owner_id = user.id
        new_car.advertisement_id = new_advertisement.id

        new_car.save()

        print(new_advertisement)
        print(new_car)

        return render(request, 'add_advertisement.html')