from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Ваше имя:',
            'email': 'Ваш Email:',
            'message': 'Введите сообщение:',
        }
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'exampleFormControlTextarea1'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Имя', 'id': 'exampleFormControlInput1'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'name@example.com', 'id': 'exampleFormControlInput2'}),
        }
