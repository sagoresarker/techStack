from django.shortcuts import render
from scanner.models import TechStack


def home(request):
    crawl_details = TechStack.objects.all()
    context = {
        'crawl_details': crawl_details,
    }
    print(crawl_details)
    return render(request, 'index.html', context)