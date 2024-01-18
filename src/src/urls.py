from django.contrib import admin
from django.urls import path

from api.views import (
    CheckListsAPIView,               
    CheckListAPIView,
    CheckListItemCreateAPIView,
    CheckListItemAPIView,                   
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', CheckListsAPIView.as_view()),
    path('api/home/<int:pk>/', CheckListAPIView.as_view()),
    path('api/home/create/', CheckListItemCreateAPIView.as_view()),
    path('api/home/checklistItem/<int:pk>/', CheckListItemAPIView.as_view()),
    
]
