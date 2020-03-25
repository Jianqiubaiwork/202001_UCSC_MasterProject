from django.shortcuts import render, HttpResponse

# Create your views here.
def scenarios_view(request):
    context = {}
    return render(request, 'scenarios.html', context)