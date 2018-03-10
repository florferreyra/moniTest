# -*- coding: utf-8 -*-
from django import forms

from .models import User


class LoanForm(forms.ModelForm):
    """
    Form of Task model.
    """
    class Meta:
        model = User
        fields = '__all__'
