from django import forms
from .models import Bokking
class DateInput(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Bokking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }
