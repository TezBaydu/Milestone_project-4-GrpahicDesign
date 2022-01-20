from django import forms
from .models import UserEnquiry


class UserEnquiryForm(forms.ModelForm):
    class Meta:
        model = UserEnquiry
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = (
                    'border-black rounded-0 text-white'
                )
