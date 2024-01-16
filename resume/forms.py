from django import forms

# Create your forms here.
class CsvUploadForm(forms.Form):
    csv_file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'class':'from-control mb-3'
            }
        )
    )