from django import forms

from first_app.models import Username


# Класс формы
class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.CharField(label='Почта')
    login = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    def save(self):
        user = Username.objects.create_user(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            login=self.cleaned_data['login'],
            password=self.cleaned_data['password']
        )
        return user
