from django.shortcuts import render

# Create your views here.

def built_in_filter(request):
    d='hAi HEllO hOw aRe YoU'
    m={'d':d}

    return render(request,'built_in_filter.html',m)