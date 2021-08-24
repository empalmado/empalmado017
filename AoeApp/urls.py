from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.loginPage, name='login'),
    # path('', views.Log_in, name='Login'),
    path('about/', views.About_us, name='about'),
    path('contact/', views.Contact_us, name='contact'),
    # path('signup/', views.Signup, name='signup'),
    path('freequotation/', views.Free_Quote, name='freequotation'),
    # path('registration/', views.Registration, name="registration"),
    # path('table/', views.Table, name='table'),
    path('table1/', views.Table1, name='table1'),
    path('update/<str:pk>/', views.update, name='update'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('warning/', views.Warning, name='warning'),

]