from django import forms


class MessageBoardForm(forms.Form):
    content = forms.CharField(label='留言簿', max_length=1024, widget=forms.Textarea(attrs={'class': 'form-control'}))
