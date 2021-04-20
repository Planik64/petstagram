from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }