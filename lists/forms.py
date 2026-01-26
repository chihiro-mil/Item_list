from django import forms
from .models import List


class Listform(forms.ModelForm):
    class Meta:
        model = List
        fields = ["title"]
        widgets = {
            "title": forms.TimeInput(attrs={
                "placeholder": "例：沖縄旅行",
                "maxlength": 20,
            })
        }
        error_messages = {
            "title": {
                "required": "タイトルを入力してください",
                "max_length": "タイトルは20文字以内で入力してください",
            }
        }