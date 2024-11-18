from django import forms
from .models import Contact, Service, Review
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField



class ContactFormModel(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id':'conName', 'placeholder': 'First name', 'autocomplete': "off"})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id':'conLName', 'placeholder': 'Last name', 'autocomplete': "off"})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id':"conEmail", 'placeholder':"Email address", 'autocomplete':"off"})
    )

    phone = FormPhoneNumberField(
        widget=forms.TextInput(attrs={
            'id': 'phone',      # Add id attribute
            'class': 'form-control',   # Add other attributes like class
            'placeholder': 'including coutry code'
        })
    )

    services = forms.ModelChoiceField(
        queryset=Service.objects.filter(available=True),
        widget=forms.Select(attrs={'id':"conService", 'class':"tj-nice-select", 'placeholder':'Choose your services'})
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'id':'conName', 'placeholder': 'Enter Subject here', 'autocomplete': "off"})
    )


    message = forms.Textarea(attrs={'id':"conMessage" ,'placeholder':"Message"})


    class Meta:
        model = Contact
        fields = '__all__'


class ReviewFormModel(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'id':'conName', 'placeholder': 'Full Name', 'autocomplete': "off"})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'id':'conLName', 'placeholder': 'Your Role Title', 'autocomplete': "off"})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id':"conEmail", 'placeholder':"Email address", 'autocomplete':"off"})
    )

    country = forms.CharField(
        widget=forms.TextInput(attrs={'id':'conName', 'placeholder': 'Enter your country', 'autocomplete': "off"})
    )

    msg = forms.Textarea(attrs={'id':"conMessage" ,'placeholder':"Message"})

    class Meta:
        model = Review
        fields = ['name', 'title', 'email', 'country', 'msg']










