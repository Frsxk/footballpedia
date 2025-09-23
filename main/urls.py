from django.urls import path
from main.views import show_main, add_employee

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('employee/', add_employee, name='add_employee'),
]