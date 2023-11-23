from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("welcome", views.welcome, name="welcome"),
    path("jeju", views.jeju, name="jeju"),
    path("seogwipo", views.seogwipo, name="seoqwipo"),
    path("memo",views.memo, name="memo"),

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

    path("BC_jeju", views.BC_jeju, name="bc"),
    path("CB_jeju", views.CB_jeju, name="cb"),
    path("CR_jeju", views.CR_jeju, name="cr"),
    path("RD_jeju", views.RD_jeju, name="rd"),
    path("TG_jeju", views.TG_jeju, name="tg"),

    path("BC_seogwipo", views.BC_seogwipo, name="bc_sw"),
    path("CB_seogwipo", views.CB_seogwipo, name="cb_sw"),
    path("CR_seogwipo", views.CR_seogwipo, name="cr_sw"),
    path("RD_seogwipo", views.RD_seogwipo, name="rd_sw"),
    path("TG_seogwipo", views.TG_seogwipo, name="tg_sw"),


    path("market_data_list", views.market_data_list, name="crop-market-data"),
    path('get-data/', views.get_data_for_date, name='get-data'),
]