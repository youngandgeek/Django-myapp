from django import forms
from .models import Booking

#create a form to collect data from user
class BookingForm (forms.ModelForm):
    class Meta:
     #pass the model class name   
     model=Booking
     #import all the fields inside the Booking model
     fields= '__all__'

 