from django.shortcuts import render
from .models import Employee

# Create your views here.
def show_main(request):
    context = {
        'application_name' : 'Footballpedia',
        'name': 'Muhammad Faza Al-Banna',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

def add_employee(request):
    employee = Employee.objects.create(
        name="Faza",
        age=19,
        persona="helloworld"
    )

    data = {
        'name': employee.name,
        'age': employee.age,
        'persona': employee.persona
    }

    return render(request, "employee.html", data)
