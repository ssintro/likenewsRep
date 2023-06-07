from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('all', views.all, name='all'),
    path('gamereview', views.gamereview, name='gamereviews'),
    path('new', views.new, name='new'),
    path('news', views.news, name='news'),
    path('popular', views.popular, name='popular'),
    path('reg', views.reg, name='reg'),
]