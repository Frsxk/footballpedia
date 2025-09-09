from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application_name' : 'Footballpedia',
        'name': 'Muhammad Faza Al-Banna',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
