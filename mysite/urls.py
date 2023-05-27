from django.urls import path
from .views import index, login_view, logout_view, about, portfolio


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('about', about, name='about'),
    path('portfolio', portfolio, name='portfolio'),
]
