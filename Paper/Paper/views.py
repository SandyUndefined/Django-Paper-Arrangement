from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


def json(request):
    return render(request, 'json.html')


json_data = ""


def files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfiles = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        file_url = fs.url(filename)
        with open(settings.MEDIA_ROOT / filename) as f:
            data = f.read()
        json_data = data
        print(json_data)
        return render(request, 'files.html', {'url': file_url})
    else:
        return render(request, 'files.html')
