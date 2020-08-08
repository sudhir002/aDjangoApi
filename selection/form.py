from django import forms


class Queryform(forms.Form):
    id = forms.CharField(label="enter query",max_length=500)
    name = forms.CharField(label="enter query",max_length=500)
