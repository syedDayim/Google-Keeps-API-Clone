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
    path('', CheckListsAPIView.as_view()),
    path('<int:pk>/', CheckListAPIView.as_view()),
    path('create/', CheckListItemCreateAPIView.as_view()),
    path('item/<int:pk>/', CheckListItemAPIView.as_view()),    
]
