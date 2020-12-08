from wsgiref.util import FileWrapper

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Paper.paper import values


def json(request):
    return render(request, 'json.html')


def files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfiles = request.FILES['files']
        fs = FileSystemStorage()
        files = fs.save(myfiles.name, myfiles)
        request.session['files'] = files
        return render(request, 'files.html')
    else:
        return render(request, 'json.html')


def multiple_files(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        myfiles = request.FILES.getlist('files')
        fs = FileSystemStorage()
        filesname = []
        for i in myfiles:
            filename = fs.save(i.name, i)
            filesname.append(filename)
        request.session['filename'] = filesname
        return render(request, 'logo.html')
    else:
        return render(request, 'files.html')


def logo(request):
    if request.method == 'POST' and request.POST.get('header') != '':
        header = request.POST.get('header')
        myfiles = request.FILES['files']
        fs = FileSystemStorage()
        logo_file = fs.save(myfiles.name, myfiles)
        # request.session['logo'] = logo
        # data retrive
        json_file = request.session.get('files', None)
        filesname = request.session.get('filename', None)
        print(
            f'This is my logo {logo_file} \n this is my header {header} \n this is my json data {json_file} \n this is my text file {filesname}')
        values(json_file, filesname, logo_file, header)
        return render(request, 'download.html')
    else:
        return render(request, 'logo.html')


def pdf_download(request):
    f = open('paper.pdf', 'rb')
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=paper.pdf'
    f.close()
    return response














