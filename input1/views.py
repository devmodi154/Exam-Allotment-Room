from django.shortcuts import render,redirect
from input1.forms import input1Form
from django.http import HttpResponse  
from django.views.generic import FormView  
from .models import Booking
# Create your views here.

# def input1_view(request):
# 	input1_form=input1Form()
# 	return render(request,'input1/input1_page.html',{'input1_form':input1_form})

class input1_view(FormView):  
    template_name = 'input1/input1_page.html'
    success_url = '/room_selection/'
    form_class = input1Form

    def form_valid(self, form):
    	return redirect('input1:room_selection_view')
    	
def room_selection_view(request):
	return render(request,'input1/room_selection_page.html')

# class room_selection_view():
# 	template_name='input1/room_selection_page.html'