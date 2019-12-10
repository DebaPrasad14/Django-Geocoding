from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

class Home(TemplateView):
	template_name = 'home.html'


def file_upload(request):
	if request.method == 'POST' and request.FILES['document']:
		myfile = request.FILES['document']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		url = fs.url(filename)
		return render(request, 'file_upload.html', {'url': url} )
	return render(request, 'file_upload.html')