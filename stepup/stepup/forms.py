from django import forms

AVAILABILITY = (
    (0, "Morning"),
    (1, "Afternoon"),
    (2, "Evening"),
    (3, "Night"),
)

class AvailabilityForm(forms.ModelForm):
    sunday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    monday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    tuesday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    wednesday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    thursday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    friday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    saturday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    def clean_my_field(self):
        return self.cleaned_data['availability'] or None

class PictureForm(forms.ModelForm):
    picture = forms.ImageField(
        label='Select an image',
        help_text='Max size 2 megabytes',
	required=False
    )

class AvailabilityandPictureForm(forms.ModelForm):
    sunday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    monday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    tuesday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    wednesday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    thursday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    friday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    saturday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple(), required=False)
    picture = forms.ImageField(
        label='Select an image',
        help_text='Max size 2 megabytes',
	required=False
    )
    def clean_my_field(self):
        return self.cleaned_data['availability'] or None
