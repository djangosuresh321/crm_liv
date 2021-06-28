from django import forms

class Emp_Form(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'name'
            }

        )
    )

    email=forms.EmailField(
        label="Enter Your EmailID",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'email'
            }
        )
    )

    sal=forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'sal'
            }
        )
    )

    mobile=forms.IntegerField(
        label="Enter Your Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'mobile'
            }
        )
    )

    location=forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'location'
            }
        )
    )