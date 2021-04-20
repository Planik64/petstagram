from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(label=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your Comment'
            }
        )
    )


