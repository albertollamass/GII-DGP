from django.urls import path, re_path
from . import controler
from django.views.generic import RedirectView

#from django.conf.urls import url

urlpatterns = [
    path('alumno/agenda/<str:estudiante>/<str:fecha>/<str:dia>', controler.agenda, name="agenda"),
    path('realizacion/<str:estudiante>/<str:fecha>/<str:dia>/<str:resultado>', controler.realizacion, name="realizacion"),
    #path('alumno/agendamas/<str:estudiante>', controler.agendamas, name="agendamas"),
    #path('alumno/agendamenos/<str:estudiante>', controler.agendamenos, name="agendamenos"),
    path('visualizar_tareas_txt/<int:tarea>/<str:estudiante>/<str:fecha>/<str:dia>', controler.visualizar_tareas_txt, name="visualizar_tareas_txt"),
    path('visualizar_tareas_img/<int:tarea>/<str:estudiante>/<str:fecha>/<str:dia>', controler.visualizar_tareas_img, name="visualizar_tareas_img"),
    path('home/', controler.index_estudiante, name="index_estudiante"),
    path('login/<str:estudiante>',controler.login_estudiante, name="login_estudiante"),
    path('login/profesor/',controler.login_profesor, name="login_profesor"),
    path('profesor/<str:profe>', controler.index_profesor, name="index_profesor"),
    path('',controler.index,name="index"),
    path('comedor/anadir_menu/<str:clase>/', controler.anadir_menu, name="anadir_menu"),
    path('comedor/', controler.comanda_general, name="comanda_general"),
    path('profesor/comanda/', controler.visualizar_comanda, name="menus_totales_profesor"),

    #url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico'))

]