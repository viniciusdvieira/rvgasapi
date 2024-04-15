# No arquivo urls.py do seu aplicativo bancos_api_app
from bancos_api_app import views
from django.urls import path
from bancos_api_app.views import listar_bancos, consultar_banco

urlpatterns = [
    path('',views.home,name='home'),
    path('bancos/', listar_bancos, name='listar_bancos'),
    path('bancos/<str:codigo_compensacao>/', consultar_banco, name='consultar_banco'),
    
]
