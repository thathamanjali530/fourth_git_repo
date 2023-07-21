from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def string_response(request):
    return HttpResponse('this is my first string')



from django.http import HttpResponse
def second_response(request):
    return HttpResponse('this is my second response')




from django.http import HttpResponse
def third_response(request):
    return HttpResponse('this is my third response')
