from django.urls import path, include
from .views import *

app_name = 'mainApp'
urlpatterns = [
    path('', index, name='index'),
    path('news/<int:page_no>/', show_all_news, name='all_news'),
    path('one_article/<int:article_id>/', show_one_article, name='one_article'),
    path('add_comment/<int:article_id>/', add_comment, name='add_comment'),
    path('detele_comment/<int:comment_id>', delete_comment, name='delete_comment')
]

handler404 = 'mainApp.views.error_404'