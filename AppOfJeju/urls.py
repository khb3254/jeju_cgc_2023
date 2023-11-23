from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
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

    path("market_data_list", views.market_data_list, name="crop-market-data"),
    path('get-data/', views.get_data_for_date, name='get-data'),
]