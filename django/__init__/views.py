from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'basis/index.html', context)

def eng_lang_view(request):
    request.session["lang"] = "eng"
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

def chn_lang_view(request):
    request.session["lang"] = "chn"
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

def http202_view(request):
    context = {}
    return render(request, 'http/http202.html', context)

def http404_view(request):
    context = {}
    return render(request, 'http/http404.html', context)