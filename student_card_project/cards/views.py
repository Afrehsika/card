from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


import barcode
from barcode.writer import ImageWriter
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render

from django.shortcuts import get_object_or_404


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('card_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'cards/student_card_form.html', {'form': form})

from django.contrib import messages

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student record deleted successfully.")
        return redirect('student_list')  # Replace 'student_list' with your actual list view name
    
    return render(request, 'cards/confirm_delete.html', {'student': student})



def generate_barcode(request, student_id):
    # Retrieve student info based on student_id
    student = Student.objects.get(pk=student_id)

    
    
    # Generate barcode
    code128 = barcode.get_barcode_class('code128')
    barcode_image = code128(student.student_number, writer=ImageWriter())
    
    # Save barcode to a BytesIO object
    buffer = BytesIO()
    barcode_image.write(buffer)
    
    # Set the response content type to image
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="barcode.png"'
    
    return response




def student_card_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('card_detail', student.id)
    else:
        form = StudentForm()
    return render(request, 'cards/student_card_form.html', {'form': form})

def card_detail_view(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'cards/card_detail.html', {'student': student})
