from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


class Home(TemplateView):
	template_name = 'home.html'


def file_upload(request):
	if request.method == 'POST' and request.FILES['document']:
		myfile = request.FILES['document']

		if not myfile.name.endswith('.xls') and not myfile.name.endswith('.xlsx'):
			messages.error(request, ('Please upload only excel file!'))
		else:
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)
			messages.success(request, ('Congrats !!! File uploaded successfully!'))
			return render(request, 'file_upload.html', {'url': url} )
	return render(request, 'file_upload.html')