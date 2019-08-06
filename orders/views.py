from django.shortcuts import render, redirect
from .models import Order
from products.models import Deal
from django.contrib import messages

def placeOrder(request):
    errors = []
    user = request.user
    dealid = int(request.POST.get("dealId"))
    deal = Deal.objects.get(pk=dealid)
    try:
        existingDeal = Order.objects.get(user=user, deal=deal, confirmed="Yes")
    except:
        discount_counter = Order.objects.filter(user=user).exclude(deal=deal).count()
        final_price = deal.discounted_price - (deal.discounted_price * discount_counter/100)
        order = Order(user=user, deal=deal, additional_discount=discount_counter, final_price=final_price)
        order.save()
        print (order)
        return render(request, "confirm.html", {"order":order})
    else:
        messages.add_message(request, messages.INFO, "You cannot buy a deal more than once")
        return redirect("products:deal")

def confirmOrder(request):
    orderId = int(request.POST.get("orderId"))
    order = Order.objects.get(pk=orderId)
    deal = order.deal

    order.confirmed = "Yes"
    order.save()

    quantity = deal.quantity - 1
    if quantity < 0:
        messages.add_message(request, messages.INFO, "Sorry, the deal just got sold off!")
        return redirect("products:deal")
    else:
        deal.quantity = quantity
        deal.save()
        messages.add_message(request, messages.INFO, "Your order has been placed! Thank you for placing the order!")
        return render(request, "confirm.html", {"order":order})
        