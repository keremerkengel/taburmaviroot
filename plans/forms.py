from django import forms
from .models import RootPlan

class RootPlanForm(forms.ModelForm):
    class Meta:
        model = RootPlan
        fields = ["city", "district", "place_type", "place_name", "visit_purpose", "visit_date", "notes"]
        widgets = {
            "visit_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "place_type": forms.Select(attrs={"class": "form-select"}),
            "place_name": forms.TextInput(attrs={"class": "form-control"}),
            "visit_purpose": forms.TextInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "city": "İl",
            "district": "İlçe",
            "place_type": "Ziyaret Türü",
            "place_name": "Yer Adı",
            "visit_purpose": "Ziyaret Amacı",
            "visit_date": "Tarih",
            "notes": "Notlar",
        }
