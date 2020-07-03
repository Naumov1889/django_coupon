from django.shortcuts import render
from .forms import CouponForm
from .models import Coupon
from django.http import HttpResponse
from django.utils.timezone import now
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)

        if form.is_valid():
            coupon = form.cleaned_data['coupon']
            shop = form.cleaned_data['shop']

            try:
                coupon_object = Coupon.objects.get(number=coupon)
            except Coupon.DoesNotExist:
                coupon_object = None

            if coupon_object:
                if coupon_object.shop:
                    messages.error(request, f'<h1 class="error">Купон недействителен</h1><h2>Купон <big>№{coupon_object.number}</big> был уже предъявлен <big>{coupon_object.used:%d-%m-%Y %H:%M}</big><br> в магазине <big>{coupon_object.shop}</big></h2>')
                elif coupon_object.deadline < now():
                    messages.error(request, f'<h1 class="error">Купон просрочен и недействителен</h1><h2>Купон <big>№{coupon_object.number}</big> должен был быть предъявлен не позднее <big>{coupon_object.deadline:%d-%m-%Y %H:%M}</big></h2>')
                else:
                    messages.success(request, '<h1 class="success">Купон действителен!</h1>')
                    coupon_object.used = now()
                    coupon_object.shop = shop
                    coupon_object.save()

            else:
                messages.error(request, "<h1 class='warning'>Номер недействителен,</h1><h2>проверьте номер и еще раз введите</h2>")

    else:
        form = CouponForm()

    return render(request, 'coupon/index.html', {'form': form})
