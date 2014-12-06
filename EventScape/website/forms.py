from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML
from crispy_forms.bootstrap import FormActions

from .models import Event, Tag

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")

        if commit:
            user.save()
        return user


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            FormActions(
                Submit('submit', 'Submit')
            )
        )


class CreateEventForm(forms.ModelForm):
    tags = forms.CharField()

    class Meta:
        model = Event
        fields = ("name", "address", "city", "state", "start", "end", "description", "tags")

    def save(self, commit=True):
        event_object = super(CreateEventForm, self).save(commit=commit)

        tags = self.cleaned_data['tags'].split()
        for tag_name in tags:
            tag_object, _ = Tag.objects.get_or_create(name=tag_name)
            tag_object.events.add(event_object)

        return event_object


    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['tags'].help_text = "Enter tags separated by spaces."
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'name',
            'address',
            'city',
            'state',
            'start',
            'end',
            'description',
            'tags',
            FormActions(
                Submit('submit', 'Submit')
            )
        )

class SearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    host = forms.CharField(required=False)
    location = forms.CharField(required=False)
    after = forms.DateTimeField(required=False)
    before = forms.DateTimeField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'keywords',
            'host',
            'location',
            'after',
            'before',
            FormActions(
                Submit('search', 'Search')
            )
        )