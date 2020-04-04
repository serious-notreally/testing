from django import forms
class CodePostForm(forms.Form):
    code = forms.CharField(required=False, widget=forms.Textarea)