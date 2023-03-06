from django import forms

class TechScannerForm(forms.Form):
    url = forms.URLField(label='Enter a URL', max_length=200)
