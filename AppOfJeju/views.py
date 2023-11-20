from django.shortcuts import render
from.models import Jeju, CropMarketData

# Create your views here.

def main_page(request):
    main_page = Jeju.objects.all()
    return render(request, "main.html", {"main_page": main_page} )

def jeju(request):
    jeju = Jeju.objects.all()
    return render(request, "jeju.html", {"jeju": jeju} )

def seogwipo(request):
    seogwipo = Jeju.objects.all()
    return render(request, "seogwipo.html", {"seogwipo": seogwipo} )

def main_of_detail(request):
    main_of_detail = Jeju.objects.all()
    return render(request, "main_of_detail.html", {"main_of_detail": main_of_detail} )

def process(request):
    process = Jeju.objects.all()
    return render(request, "process.html", {"process": process} )

def resume(request):
    resume = Jeju.objects.all()
    return render(request, "resume.html", {"resume": resume} )

def code(request):
    code = Jeju.objects.all()
    return render(request, "code.html", {"code": code} )

def jcarrot(request):
    jcarrot = Jeju.objects.all()
    return render(request, "detail/jeju/carrot_jeju.html", {"jcarrot": jcarrot} )

# Create your views here.
def crop_market_data_view(request):
    data = CropMarketData.objects.all()
    return render(request, 'calender.html', {'data':data})