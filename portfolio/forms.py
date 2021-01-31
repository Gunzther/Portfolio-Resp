from django import forms


class QuestionForm(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name'}), max_length=200)
    your_email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    your_question = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message...'}), max_length=200)
