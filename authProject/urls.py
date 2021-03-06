"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.contrib                  import admin                                   # Importacion de la vista de administracion
from django.urls                     import path                                    # Importacion de la clase urls de Django
from rest_framework_simplejwt.views  import (TokenObtainPairView, TokenRefreshView) # Importacion de las views simple JWT
from authApp                        import views                                    # Importacion de las vistas de la app 

urlpatterns = [
    path('admin/', admin.site.urls),                              # Url del sitio de administracion 
    path('login/', TokenObtainPairView.as_view()),                # Url login de usuario 
    path('refresh/', TokenRefreshView.as_view()),                 # Ulr otener toquen refresh
    path('verifyToken/', views.VerifyTokenView.as_view()),        # Url verificar toquen 
    path('userRegister/', views.UserCreateView.as_view()),        # Url para registro de usuarios
    path('user/<int:pk>/', views.UserDetailView.as_view()),       # Url para ver perfil de usuaario 
    path('userUpdate/<int:pk>/', views.UserUpdateView.as_view()), # Url para actualizar perfil de usuario 
]
