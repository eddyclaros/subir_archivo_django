from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from subirword.models import ArchivoClausula

# Create your views here.
class SubirWord():
    def subirword(request):
        if request.method=='POST' and request.FILES['myfile']:
            nombre=request.POST['filename']
            print("entra")
            myfile=request.FILES['myfile']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            uploaded_file_url=fs.url(filename)

            clausulas=ArchivoClausula()
            clausulas.title=nombre
            clausulas.file=uploaded_file_url
            clausulas.save()
            clausulas=ArchivoClausula.objects.all()
            return render(request, 'paginas/subir.html',{'clausulas':clausulas})
        clausulas=ArchivoClausula.objects.all()
        return render(request,"paginas/subir.html",{'clausulas':clausulas})