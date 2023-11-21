from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("jeju", views.jeju, name="jeju"),
    path("seogwipo", views.seogwipo, name="seoqwipo"),
    path("main_of_detail", views.main_of_detail, name="main_of_detail"),
    path("process", views.process, name="process"),
    path("resume", views.resume, name="resume"),
    path("code",views.code, name="code"),
    path("carrot_jeju", views.jcarrot, name="jcarrot"),
    path("cabbage_jeju", views.jcabbage, name="jcabbage"),
    path("mandarin_jeju", views.jmandarin, name="jmandarin"),
    path("broccoli_jeju", views.jbroccoli, name="jbroccoli"),
    path("radish_jeju", views.jradish, name="jradish"),

    path("carrot_seogwipo", views.scarrot, name="scarrot"),
    path("cabbage_seogwipo", views.scabbage, name="scabbage"),
    path("mandarin_seogwipo", views.smandarin, name="smandarin"),
    path("broccoli_seogwipo", views.sbroccoli, name="sbroccoli"),
    path("radish_seogwipo", views.sradish, name="sradish"),

    path("crop_market_data_view", views.crop_market_data_view, name="crop-market-data"),
]