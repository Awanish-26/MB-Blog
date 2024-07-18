from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username...'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password...'}))


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password...'}))


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Your old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Your new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Your new password repeat'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Enter your name here...'}),
            "content": forms.Textarea(attrs={"rows": 12, 'placeholder': 'Enter your text here...'}),
        }


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['banner', 'title', 'content']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Enter your name here...'}),
            "content": forms.Textarea(attrs={"rows": 12, 'placeholder': 'Enter your text here...'}),
        }


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
