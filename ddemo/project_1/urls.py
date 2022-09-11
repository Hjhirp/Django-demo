from django.urls import path 
from . import views

urlpatterns = [
	path('project_1/',views.index, name='project_1'),
	path('project_1/2',views.secondformat, name='project_1_2')																												
]