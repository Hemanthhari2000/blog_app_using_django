from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import BlogPost


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'title',
                    'type': 'text',
                    'id': 'titleInput',
                    'placeholder': "Title"
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'content',
                    'type': 'text',
                    'id': 'contentInput',
                    'placeholder': "Content",
                    'style': 'height: 400px'
                }
            )
        }
