from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("welcome", views.welcome, name="welcome"),
    path("retail", views.jeju, name="jeju"),
    path("whole", views.seogwipo, name="seoqwipo"),
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

    path("BC_retail", views.BC_jeju, name="bc"),
    path("CB_retail", views.CB_jeju, name="cb"),
    path("CR_retail", views.CR_jeju, name="cr"),
    path("RD_retail", views.RD_jeju, name="rd"),
    path("TG_retail", views.TG_jeju, name="tg"),

    path("BC_whole", views.BC_seogwipo, name="bc_sw"),
    path("CB_whole", views.CB_seogwipo, name="cb_sw"),
    path("CR_whole", views.CR_seogwipo, name="cr_sw"),
    path("RD_whole", views.RD_seogwipo, name="rd_sw"),
    path("TG_whole", views.TG_seogwipo, name="tg_sw"),


    path("market_data_list", views.market_data_list, name="crop-market-data"),
    # AJAX 요청을 위한 URL 패턴 추가
    path("whole/", views.get_predictions_whole, name="get_predictions_whole"),
    path("BC_whole/", views.get_predictions_whole, name="bc_get_predictions_whole"),
    path("CB_whole/", views.get_predictions_whole, name="cb_get_predictions_whole"),
    path("CR_whole/", views.get_predictions_whole, name="cr_get_predictions_whole"),
    path("RD_whole/", views.get_predictions_whole, name="rd_get_predictions_whole"),
    path("TG_whole/", views.get_predictions_whole, name="tg_get_predictions_whole"),

    path("retail/", views.get_predictions_retail, name="get_predictions_retail"),
    path("BC_retail/", views.get_predictions_retail, name="bc_get_predictions_retail"),
    path("CB_retail/", views.get_predictions_retail, name="cb_get_predictions_retail"),
    path("CR_retail/", views.get_predictions_retail, name="cr_get_predictions_retail"),
    path("RD_retail/", views.get_predictions_retail, name="rd_get_predictions_retail"),
    path("TG_retail/", views.get_predictions_retail, name="tg_get_predictions_retail"),
]