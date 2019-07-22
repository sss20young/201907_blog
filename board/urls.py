from django.contrib import admin
from django.urls import path
import board.views

urlpatterns = [
    path('post/', board.views.post, name='post'),
    path('', board.views.home, name='home'),
    path('<int:board_id>/', board.views.detail, name='detail'),
    path('show/', board.views.show, name='show'),
    path('<int:pk>/edit/', board.views.edit, name='edit'),
    path('<int:pk>/delete/', board.views.delete, name='delete'),
]