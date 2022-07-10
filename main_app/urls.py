
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_bloom/', views.add_bloom, name='add_bloom'),
    path('plants/<int:plant_id>/assoc_condition/<int:condition_id>/', views.assoc_condition, name='assoc_condition'),
    path('plants/<int:plant_id>/assoc_condition/<int:condition_id>/delete', views.assoc_condition_delete, name='assoc_condition_delete'),
    path('conditions/', views.ConditionList.as_view(), name='conditions_index'),
    path('conditions/<int:pk>/', views.ConditionDetail.as_view(), name='conditions_detail'),
    path('conditions/create/', views.ConditionCreate.as_view(), name='conditions_create'),
    path('conditions/<int:pk>/update/', views.ConditionUpdate.as_view(), name='conditions_update'),
    path('conditions/<int:pk>/delete/', views.ConditionDelete.as_view(), name='conditions_delete'),
    path('plants/<int:plant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]