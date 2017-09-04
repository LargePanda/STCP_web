from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import time
import cctk_data.convert
import cctk_data.interface
print "loaded"
# Create your views here.


def index(request):
    return render(request, 'index.html')

def query_char(request, qchar):
    return JsonResponse(cctk_data.interface.get_info(qchar))

def convert(request):
    source = request.GET.get('text', None)
    target = source
    target = cctk_data.convert.change(target)
    data = {'text': target}
    return JsonResponse(data)
