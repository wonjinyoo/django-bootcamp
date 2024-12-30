from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord, Webpage, Topic


# Create your views here.
def index(request):
    
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'AppTwo/index.html', context=date_dict)
