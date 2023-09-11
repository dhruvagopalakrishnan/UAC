from secrets import choice
from django import forms
from numpy import require
from base import models
import qrcode
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User


class SaveBookings(forms.ModelForm):
    flight = forms.CharField(max_length=250)
    type = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    midle_name = forms.CharField(max_length=250, required=False)
    last_name = forms.CharField(max_length=250)
    gender = forms.CharField(max_length=250)
    contact = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    address = forms.Textarea()


    class Meta:
        model = models.Bookings
        fields = ('flight','type','first_name', 'midle_name', 'last_name', 'gender', 'contact', 'email', 'address', )

    def clean_flight(self):
        fid = self.cleaned_data['flight']
        try:
            flight = models.Shuttles.objects.get(id = fid)
            return flight
        except:
            raise forms.ValidationError(f"Invalid Flight")

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = ['email', ]
class SaveTransport(forms.ModelForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    contact = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    address = forms.Textarea()
    ship_type = forms.CharField(max_length=250)
    weight = forms.CharField(max_length=250)

    class Meta:
        model = models.Transport
        fields =  '__all__'
