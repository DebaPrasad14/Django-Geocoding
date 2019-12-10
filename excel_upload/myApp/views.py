from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Home(TemplateView):
	template_name = 'home.html'


def file_upload(request):
    return render(request, 'file_upload.html')