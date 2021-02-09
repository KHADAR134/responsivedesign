from django.shortcuts import render

# Create your views here.

def responsivewebsite(request):
    context = {}
    return render(request, 'responsive/responsivewebsite.html', context)
