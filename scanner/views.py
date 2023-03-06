from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TechScannerForm
from .models import TechStack
import requests
from django.db.utils import IntegrityError
import json
from Wappalyzer import Wappalyzer, WebPage


def scan(request):
    if request.method == 'POST':
        form = TechScannerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                tech_info = {}
  
                wappalyzer = Wappalyzer.latest()
                webpage = WebPage.new_from_url(url)
                wappalyzer.analyze(webpage)

                webpage = WebPage.new_from_url(url)
                wappalyzer_res = wappalyzer.analyze_with_categories(webpage)

                tech_stack = TechStack(url=url, tech_info=json.dumps(wappalyzer_res))
                tech_stack.save()
                tech_data = json.dumps(wappalyzer_res)

                context = {
                    'tech_data': tech_data,
                }
                
                print(tech_data)
                return render(request, 'scanner/scan_result.html', context=context)
                
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error: {str(e)}")
            except IntegrityError:
                return HttpResponse("Error: This URL already exists in the database.")
    else:
        form = TechScannerForm()
    return render(request, 'scanner/scanner.html', {'form': form})




def scan_result(request, pk):
    tech_stack = TechStack.objects.get(id=pk)
    tech_info = json.loads(tech_stack.tech_info)
    return render(request, 'scanner/scan_result.html', {'tech_info': tech_info})