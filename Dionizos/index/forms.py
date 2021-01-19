from django import forms
from index.models import Wines, Comments


class WineForm(forms.ModelForm):
    class Meta:
        def __init__(self):
            self.fields['image'].required = False

        model = Wines
        fields = ["name",
                  "price",
                  "color",
                  "taste",
                  "descriptions",
                  "image"]
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
    fraze = forms.CharField(required=False, label="",widget=forms.widgets.TextInput(attrs={"placeholder":"Szukaj",
                                                                  "class":"form-control",
                                                                  "style":"width:200px;display:inline;"}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('nickname', 'description')

