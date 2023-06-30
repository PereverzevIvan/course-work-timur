from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок', id='title')
    text = forms.Textarea()
    price = forms.IntegerField()
    image = forms.FileField()