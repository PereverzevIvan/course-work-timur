from django.urls import path, include
from .views import *

app_name = 'mainApp'
urlpatterns = [
    path('', index, name='index'),
    path('news/', show_all_news, name='all_news'),
    path('one_article/<int:article_id>/', show_one_article, name='one_article'),
    path('add_comment/<int:article_id>/', add_comment, name='add_comment'),
    path('detele_comment/<int:comment_id>', delete_comment, name='delete_comment'),
    path('advertisements/', show_all_advertisements, name='all_advertisements'),
    path('one_advertisement/<int:advertisement_id>', show_one_advertisement, name='one_advertisement'),
    path('add_advertisement/', add_advertisement, name='add_advertisement'),
]

handler404 = 'mainApp.views.error_404'