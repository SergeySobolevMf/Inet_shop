from django.db import models
from django.shortcuts import render, get_object_or_404

from .models import Mobile, Group

def index(request):
    template = 'main/index.html'
    mobile = Mobile.objects.all()
    context = {
        'mobile_phones':mobile
    }
    return render(request, template, context)


def get_list(request, slug):
    template = 'main/mobile.html'
    group = get_object_or_404(Group, slug=slug)
    mobile = group.mobiles.all()
    context = {
        'mobile_phones':mobile
    }
    return render(request, template, context)