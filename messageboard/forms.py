from django import forms


class MessageBoardForm(forms.Form):
    username = forms.CharField(label='匿名', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='内容', max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control'}))
