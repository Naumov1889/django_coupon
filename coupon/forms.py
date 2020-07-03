from django import forms
from .models import Shop, Coupon


class CouponForm(forms.Form):
    coupon = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Введите номер',
            'id': 'coupon'}),
        label='')
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(),
                                  empty_label="Выберите магазин...",
                                  label='',
                                  widget=forms.Select(attrs={'id': 'shop'}))
