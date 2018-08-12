from django import forms


class CommentsForm(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name...'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment...'}))