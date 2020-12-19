from django import forms
from index.models import Wines


class WineForm(forms.ModelForm):
    class Meta:
        model = Wines
        fields = ["name",
                  "price",
                  "color",
                  "taste",
                  "descriptions",
                  "picture"]
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
                   "descriptions": forms.widgets.TextInput(attrs={"class": "form-control",
                                                                "cols": 50,
                                                                "rows": 8}),
                   "picture": forms.widgets.TextInput(attrs={"class": "form-control",
                                                                "cols": 50,
                                                                "rows": 8})}