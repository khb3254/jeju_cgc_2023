from django.shortcuts import render
from.models import Jeju, CropMarketData

# Create your views here.

def main_page(request):
    main_page = Jeju.objects.all()
    return render(request, "main.html", {"main_page": main_page} )

def welcome(request):
    welcome = Jeju.objects.all()
    return render(request, "welcome.html", {"welcome": welcome} )


def jeju(request):
    jeju = Jeju.objects.all()
    return render(request, "jeju.html", {"jeju": jeju} )

def seogwipo(request):
    seogwipo = Jeju.objects.all()
    return render(request, "seogwipo.html", {"seogwipo": seogwipo} )


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

def memo(request):
    memo = Jeju.objects.all()
    return render(request, "memo.html", {"memo": memo} )



# Create your views here.
def crop_market_data_view(request):
    data = CropMarketData.objects.all()
    return render(request, 'calender.html', {'data':data})

def BC_jeju(request):
    bc = Jeju.objects.all()
    return render(request, "main/jeju/BC_jeju.html", {"bc": bc} )

def CB_jeju(request):
    cb = Jeju.objects.all()
    return render(request, "main/jeju/CB_jeju.html", {"cb": cb} )

def CR_jeju(request):
    cr = Jeju.objects.all()
    return render(request, "main/jeju/CR_jeju.html", {"cr": cr} )

def RD_jeju(request):
    rd = Jeju.objects.all()
    return render(request, "main/jeju/RD_jeju.html", {"rd": rd} )

def TG_jeju(request):
    tg = Jeju.objects.all()
    return render(request, "main/jeju/TG_jeju.html", {"tg": tg} )



def BC_seogwipo(request):
    bc_s = Jeju.objects.all()
    return render(request, "main/seogwipo/BC_seogwipo.html", {"bc_s": bc_s} )

def CB_seogwipo(request):
    cb_s = Jeju.objects.all()
    return render(request, "main/seogwipo/CB_seogwipo.html", {"cb_s": cb_s} )

def CR_seogwipo(request):
    cr_s = Jeju.objects.all()
    return render(request, "main/seogwipo/CR_seogwipo.html", {"cr_s": cr_s} )

def RD_seogwipo(request):
    rd_s = Jeju.objects.all()
    return render(request, "main/seogwipo/RD_seogwipo.html", {"rd_s": rd_s} )

def TG_seogwipo(request):
    tg_s = Jeju.objects.all()
    return render(request, "main/seogwipo/TG_seogwipo.html", {"tg_s": tg_s} )