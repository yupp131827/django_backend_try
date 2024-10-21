from django.urls import path

from api.views import getArticleApiView

app_name = 'api'
urlpatterns = [
    path('article/<str:article_id>', getArticleApiView.getArticleApi_, name='article'),
    path('article', getArticleApiView.getArticleListApi_, name='article_list'),



    # path('ajax/detail', bookingViews.ajax_staff, name='ajax-detail'),

]