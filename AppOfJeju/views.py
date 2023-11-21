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

def jbroccoli(request):
    jbroccoli = Jeju.objects.all()
    return render(request, "detail/jeju/broccoli_jeju.html", {"jbroccoli": jbroccoli} )

def jcabbage(request):
    jcabbage = Jeju.objects.all()
    return render(request, "detail/jeju/cabbage_jeju.html", {"jcabbage": jcabbage} )

def jmandarin(request):
    jmandarin = Jeju.objects.all()
    return render(request, "detail/jeju/mandarin_jeju.html", {"jmandarin": jmandarin} )

def jradish(request):
    jradish = Jeju.objects.all()
    return render(request, "detail/jeju/radish_jeju.html", {"jradish": jradish} )



def scarrot(request):
    scarrot = Jeju.objects.all()
    return render(request, "detail/seogwipo/carrot_seogwipo.html", {"scarrot": scarrot} )

def sbroccoli(request):
    sbroccoli = Jeju.objects.all()
    return render(request, "detail/seogwipo/broccoli_seogwipo.html", {"sbroccoli": sbroccoli} )

def scabbage(request):
    scabbage = Jeju.objects.all()
    return render(request, "detail/seogwipo/cabbage_seogwipo.html", {"scabbage": scabbage} )

def smandarin(request):
    smandarin = Jeju.objects.all()
    return render(request, "detail/seogwipo/mandarin_seogwipo.html", {"smandarin": smandarin} )

def sradish(request):
    sradish = Jeju.objects.all()
    return render(request, "detail/seogwipo/radish_seogwipo.html", {"sradish": sradish} )




# Create your views here.
def crop_market_data_view(request):
    data = CropMarketData.objects.all()
    return render(request, 'calender.html', {'data':data})