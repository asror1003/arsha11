import datetime

from django.shortcuts import render
from django.db.models import Q
from myfiles.models import *
# Create your views here.
def index(malumot):

    if 'subject' in malumot.POST:
        ismi = malumot.POST.get('name')
        mail = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()

        Murojat(nomi=ismi,mail=mail,title=mavzu,text=xabar,date=vaqt).save()
    if 'soz' in malumot.POST:
        text = str(malumot.POST.get('soz'))
        text = text.strip()
        qidirish = Q(nomi__startswith = text) | Q(company__startswith = text) |\
                   Q(url__startswith = text) | Q(date__startswith = text) |\
                   Q(tur__nomi__startswith = text) | Q(malumot__startswith = text)
        qidirish1 = Q(nomi__startswith = text)
        works = Portfolio.objects.filter(qidirish)
        turlar = Type.objects.filter(qidirish1)
        return render(malumot, 'index.html', {'works': works, "types": turlar})

    works = Portfolio.objects.all()
    turlar = Type.objects.all()
    workc = Team.objects.all()
    return render(malumot,'index.html',{'works':works,"types":turlar,"teams":workc})



def filter_index(malumot,id):
    works = Portfolio.objects.filter(tur_id=id)
    turlar = Type.objects.all()
    return render(malumot, 'index.html', {'works': works, "types": turlar})

def portfolio(malumot):
    return render(malumot,'portfolio-details.html')

def single_portfolio(malumot,id):
    work = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':work})

