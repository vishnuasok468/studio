
from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name='home'),
    path('d_login',views.d_login,name='d_login'),
    path('d_reg',views.d_reg,name='d_reg'),
    path('login',views.login,name='login'),
    path('reg',views.reg,name='reg'),
    path('equip',views.equip,name='equip'),
    path('booknow',views.booknow,name='booknow'),
    path('booknowbtn',views.booknowbtn,name='booknowbtn'),
    path('about',views.about,name='about'),

]
