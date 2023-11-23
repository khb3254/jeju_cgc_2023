from django.shortcuts import render
from.models import Jeju, CropMarketData, PredictionData
from django.template.loader import render_to_string
from django.http import HttpResponse
from datetime import datetime

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

def get_data_for_date(request):
    selected_date = request.GET.get('date')

    try:
        # 날짜 형식 검증
        valid_date = datetime.strptime(selected_date, '%Y-%m-%d')
    except ValueError:
        # 날짜 형식이 잘못된 경우 적절한 응답 반환
        return HttpResponse("Invalid date format", status=400)

    data_queryset = PredictionData.objects.filter(crop_date=selected_date)
    context = {'data': data_queryset}
    html = render_to_string('calender.html', {'data': data_queryset})
    return HttpResponse(html)

def market_data_list(request):
    market_data = CropMarketData.objects.all()
    return render(request, 'calender.html', {'market_data':market_data})