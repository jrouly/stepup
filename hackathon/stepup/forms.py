from django import forms

AVAILABILITY = (
    (0, "Morning"),
    (1, "Afternoon"),
    (2, "Evening"),
    (3, "Night"),
)

class AvailabilityForm(forms.ModelForm):
    sunday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    monday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    tuesday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    wednesday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    thursday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    friday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    saturday = forms.MultipleChoiceField(choices=AVAILABILITY, widget=forms.CheckboxSelectMultiple())
    def clean_my_field(self):
        return self.cleaned_data['availability']
