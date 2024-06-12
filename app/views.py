from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.form import *
# Create your views here.

class DataInsertByTv(TemplateView):
    template_name='DataInsertByTv.html'
    
    def get_context_data(self, **kwargs): 
        ECDO=super().get_context_data(**kwargs)
        #ECDO['name']='Ashu'
        #ECDO['age']=3
        #return ECDO
        ECDO['ECFO']=CollegeForm()
        return ECDO

#FORMVIEW


    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('DataInsertByTV is done')
        else:
            return HttpResponse('DataInsertByTV not done')
        
class InsertDataByFv(FormView):
    template_name='InsertDataByFv.html'
    form_class=CollegeForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('formview is done successfully')
