from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser, Pushes, Options


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class PushForm(forms.ModelForm):
    sent_at = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%y'),
        input_formats=('%d/%m/%y',)
    )

    def __init__(self, *args, **kwargs):
        super(PushForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.help_text

    class Meta:
        model = Pushes
        fields = ['title', 'text', 'picture', 'sent_at', 'name']
        labels = {
            'picture': _('Изображение уведомления'),
        }


class OptionsForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = ['name', 'value']
