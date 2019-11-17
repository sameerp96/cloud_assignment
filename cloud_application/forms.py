from django import forms


class AirpollutionForm(forms.ModelForm):
    class meta:
        model = AirPollution
        feilds = ('country', 'state', 'city', 'place', 'pollution')