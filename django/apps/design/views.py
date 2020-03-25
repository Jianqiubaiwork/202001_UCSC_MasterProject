from django.shortcuts import render, HttpResponse

# Create your views here.
def design_view(request):
    context = {}
    return render(request, 'design.html', context)