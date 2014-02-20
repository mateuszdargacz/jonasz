# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse


def home(request):
    context = {'text':"jakis text"}

    return TemplateResponse(request,'reservation/sites/home.html',context)