from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('licenciatura/<int:id>/', views.licenciatura_detail, name='licenciatura_detail'),
    path('unidade-curricular/<int:id>/', views.unidade_curricular_detail, name='unidade_curricular_detail'),
    path('projeto/<int:id>/', views.projeto_detail, name='projeto_detail'),
    path('tecnologia/<int:id>/', views.tecnologia_detail, name='tecnologia_detail'),
    path('tfc/<int:id>/', views.tfc_detail, name='tfc_detail'),
    path('competencia/<int:id>/', views.competencia_detail, name='competencia_detail'),
    path('formacao/<int:id>/', views.formacao_detail, name='formacao_detail'),
    path('makingof/<int:id>/', views.makingof_detail, name='makingof_detail'),
    path('docente/<int:id>/', views.docente_detail, name='docente_detail'),
    path('area-interesse/<int:id>/', views.area_interesse_detail, name='area_interesse_detail'),
    path('midia/<int:id>/', views.midia_detail, name='midia_detail'),
]