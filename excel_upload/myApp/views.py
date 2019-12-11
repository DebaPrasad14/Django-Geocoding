from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


class Home(TemplateView):
	template_name = 'home.html'


def file_upload(request):
	if request.method == 'POST':
		if not request.FILES.get('document'):
			messages.error(request, ('You have not selected any File. Please select a file to upload!'))
		else:
			myfile = request.FILES.get('document')
			if not myfile.name.endswith('.xls') and not myfile.name.endswith('.xlsx'):
				messages.error(request, ('Please upload only excel file!'))
			else:
				fs = FileSystemStorage()
				filename = fs.save(myfile.name, myfile)
				url = fs.url(filename)
				messages.success(request, ('Congrats !!! File uploaded successfully!'))
				return render(request, 'file_upload.html', {'url': url} )
	return render(request, 'file_upload.html')