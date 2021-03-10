from mysite.settings import TEMPLATES
from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView, TemplateView
from .models import Videoinfo


# Create your views here.


class BaseView(TemplateView):
    template_name = 'arikui/base.html'

class Videoinfo(ListView):
    models = Videoinfo
    template_name = 'arikui/base.html'


    