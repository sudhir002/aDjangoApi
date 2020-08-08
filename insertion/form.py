from django import forms


class Queryform(forms.Form):
    id = forms.CharField(label="enter val",max_length=500)
    real_name= forms.CharField(label="enter val",max_length=500)
    tz = forms.CharField(label="enter val",max_length=500)
    start_time = forms.CharField(label="enter val",max_length=500)
    end_time = forms.CharField(label="enter val",max_length=500)

