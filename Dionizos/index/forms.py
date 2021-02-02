from django import forms
from index.models import Wine, Comment, Color, Taste, WineImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WineForm(forms.ModelForm):
    class Meta:
        def __init__(self):
            self.fields['image'].required = False

        model = Wine
        fields = ["name",
                  "price",
                  "color",
                  "taste",
                  "descriptions",
                  "pictures"]
        widgets = {"name": forms.widgets.TextInput(attrs={"class": "form-control",
                                                                "cols": 50,
                                                                "rows": 8}),
                   "price": forms.widgets.NumberInput(attrs={"class": "form-control",
                                                            "cols": 50,
                                                            "rows": 8}),
                   "color": forms.widgets.Select(attrs={"class": "form-control",
                                                         "style": "width:120px;"}),
                   "taste": forms.widgets.Select(attrs={"class": "form-control",
                                                           "style": "width:120px;"}),
                   "descriptions": forms.widgets.Textarea(attrs={"class": "form-control",
                                                                "cols": 40,
                                                                "rows": 4})}
                
# formularz przeszukiwania na głównej stronie                                                         
class SearchForm(forms.Form):
    fraze = forms.CharField(required=False, label="",widget=forms.widgets.TextInput(attrs={"placeholder":"Szukaj nazwy...",
                                                                  "class":"form-control",
                                                                 "style":"width:200px;display:inline;"}))

    
    color = forms.ModelChoiceField(required=False,
                                      queryset=Color.objects.all(),
                                      label_suffix="",
                                      empty_label="Kolor",
                                      label="",
                                      widget=forms.widgets.Select(attrs={"class": "form-control","style":"width:160px;"}))

    taste = forms.ModelChoiceField(required=False,
                                      queryset=Taste.objects.all(),
                                      label_suffix="",
                                      empty_label="Smak",
                                      label="Taste",
                                      widget=forms.widgets.Select(attrs={"class": "form-control","style":"width:160px;"}))

    price_min = forms.DecimalField(max_digits=6, decimal_places=2,
                                    required=False,
                                    label = "",
                                    widget=forms.widgets.NumberInput(attrs={'placeholder': 'Cena od',"class": "form-control","style":"width:160px;"}))

    price_max = forms.DecimalField(max_digits=6, decimal_places=2,
                                  required=False,
                                  widget=forms.widgets.NumberInput(attrs={'placeholder': 'Cena do',"class": "form-control","style":"width:160px;"}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["nickname",
                  "description"]

        widgets = {"nickname": forms.widgets.TextInput(attrs={"class": "form-control",
                                                                "cols": 50,
                                                                "rows": 8}),
                   "description": forms.widgets.Textarea(attrs={"class": "form-control",
                                                                    "cols": 40,
                                                                    "rows": 4}),}
class ImageForm(forms.ModelForm):
    class Meta:
        model = WineImage
        fields = ["wineimage"]

        widgets = {"wineimage": forms.widgets.FileInput(),}


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user