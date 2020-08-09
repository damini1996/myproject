from django import forms
INTEGER_CHOICES = [tuple([x,x]) for x in range(1,32)]

class Addblogs(forms.Form):
    title = forms.CharField()
    post = forms.CharField(widget= forms.Textarea)
    user = forms.CharField(label='Select User id', widget=forms.Select(choices= INTEGER_CHOICES))
    #static dropdown



    

