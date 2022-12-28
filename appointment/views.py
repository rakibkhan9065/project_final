from django.shortcuts import render
from django.contrib import messages
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import PatientForm, PatientAppointmentAnswerForm
from .models import Patients, Doctor, PatientAppointmentAnswer


# Create your views here.
# @api_view(['POST',])

def create_view(request):
  default_user = {
    'user':request.user
  }

  form = PatientForm(initial=default_user)
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Create successfully.')
      return redirect('/')
  return render(request, 'appointment/home.html', {'form': form})


# AJAX
def load_doctors(request):
  department_id = request.GET.get('department_id')
  doctors = Doctor.objects.filter(department_id=department_id).all()
  return render(request, 'appointment/doctor_dropdown_list_options.html', {'doctors': doctors})


def total_appointments(request):
  total = Patients.objects.all()


  context ={
    'total': total
  }
  return render(request ,'appointment/appointment_list.html', context)

 
def user_appointments(request,_id):
  try:
    data = Patients.objects.get(id =_id)
    answers = PatientAppointmentAnswer.objects.filter(patient = data)
  except Patients.DoesNotExist:
    raise Http404('Data does not exist')
    
  if request.method == 'POST':
    form = PatientAppointmentAnswerForm(request.POST)
    if form.is_valid():
      answers = PatientAppointmentAnswer(
      test=form.cleaned_data['test'],
      medicine_one=form.cleaned_data['medicine_one'],
      medicine_two=form.cleaned_data['medicine_two'],
      medicine_three=form.cleaned_data['medicine_three'],
      medicine_others=form.cleaned_data['medicine_others'],
      advice=form.cleaned_data['advice'],
      patient=data)
      answers.save()
      messages.success(request, 'successfully request for appointment.')
      return redirect(f'/')
  else:
      form = PatientAppointmentAnswerForm()

  context = {
    'data':data,
    'form':form,
    'answers':answers,
  }
  return render(request,'appointment/appointment_details.html',context)