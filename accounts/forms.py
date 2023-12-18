from django import forms
from .models import Account

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'p-2 rounded-xl border w-full',
        'placeholder': 'Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'p-2 rounded-xl border w-full',
        'placeholder' : 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['full_name','email']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'p-2 mt-3 rounded-xl border'
        self.fields['email'].widget.attrs['class'] = 'p-2 rounded-xl border'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(
                'Password doesnot match'
            )
