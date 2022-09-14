from django import forms


class SignupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}),
                           required=True)
    email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}),
                            required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}),
                               required=True)
    phone = forms.CharField(label='Phone', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}),
                            required=True)
    address = forms.CharField(label='Address', max_length=100,
                              widget=forms.Textarea(attrs={'class': "form-control", 'rows': "3"}),
                              required=False)
