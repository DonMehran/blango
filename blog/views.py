from django.shortcuts import render
# from django.request import Request
# Create your views here.
def index(request) -> render:
  return render(request, 'blog/index.html')