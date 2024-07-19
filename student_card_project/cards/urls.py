from django.urls import path
from .views import student_card_view, card_detail_view,edit_student, delete_student

from .views import generate_barcode


    


urlpatterns = [
    path('create/', student_card_view, name='create_card'),
    path('card/<int:pk>/', card_detail_view, name='card_detail'),
    path('student/edit/<int:pk>/', edit_student, name='edit_student'),
    path('student/delete/<int:pk>/', delete_student, name='delete_student'),
    path('barcode/<int:student_id>/', generate_barcode, name='generate_barcode'),
    
   
]
