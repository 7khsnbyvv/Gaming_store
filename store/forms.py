from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Parol kiriting', 'class': 'form-input'}),
        label="Parol"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Parolni qayta kiriting', 'class': 'form-input'}),
        label="Parolni tasdiqlang"
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Foydalanuvchi nomi', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email manzilingiz', 'class': 'form-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Kiritilgan parollar bir-biriga mos kelmadi!")
        return cleaned_data