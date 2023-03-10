from django import forms


class BirthdayForm(forms.Form):
    birthday = forms.DateField(
        label='Введите дату',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    submit = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'type': 'submit', 'class': 'btn btn-primary card-button'})
    )