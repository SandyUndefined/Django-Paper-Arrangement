from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


def json(request):
    return render(request, 'json.html')


json_file = ""
filesname = []
logo_file = ""
header = ""


def files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfiles = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        json_file = filename
        print(json_file)
        return render(request, 'files.html')
    else:
        return render(request, 'json.html')


def multiple_files(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        myfiles = request.FILES.getlist('files')
        fs = FileSystemStorage()
        for i in myfiles:
            filename = fs.save(i.name, i)
            filesname.append(filename)
        print(filesname)
        return render(request, 'logo.html')
    else:
        return render(request, 'files.html')


def logo(request):
    if request.method == 'POST' and request.POST.get('header') != '':
        header = request.POST.get('header')
        myfiles = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        logo_file = filename
        print(logo_file)
        print(header)
        return render(request, 'download.html')
    else:
        return render(request, 'logo.html')
