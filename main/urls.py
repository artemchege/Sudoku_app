from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.SudokuMain.as_view(), name='main'),
    path('result/<int:id>', views.SudokuResult.as_view(), name='result'),
    path('history/', views.SudokuHistory.as_view(), name='history'),
]