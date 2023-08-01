from django import forms


class ProductCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)



