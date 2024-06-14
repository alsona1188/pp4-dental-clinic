from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .forms import AppointmentForm
from .models import AppointmentRequest
from django.contrib import messages



@login_required
def appointment_request(request):
    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            appointment_form = AppointmentForm()
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for booking with us!"
            )
        else:
            messages.add_message(
            request, messages.ERROR,
            "This time slot is not available! Try another one, or you can call us: +49 345 678912")

    appointment_form = AppointmentForm()


    return render(
        request,
        "appointment/appointment.html",
        {
            "appointment_form": appointment_form
        },
    )


@receiver(pre_save, sender=AppointmentRequest)
def set_current_user(sender, instance, *args, **kwargs):
    if not instance.user_id:
        instance.user = get_current_user() 