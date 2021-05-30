from django.contrib import messages
from .models import Contact
from django.shortcuts import render, redirect
from django.core.mail import send_mail


def contact(request):
    if(request.method == 'POST'):
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        seller_email = request.POST['seller_email']

        if(request.user.is_authenticated):
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if(has_contacted):
                messages.error(request, 'You have already made an enquiry for this property!')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail(
            'Property Listing Enquiry',
            'There has been an enquiry for ' + listing + ' from ' + name + '(' + email + ')' '\n' 'Message: ' + message + '.',
            'guptasarthak9292@gmail.com',
            [seller_email, 'sarthakguptasg9292@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will contact you soon!')

        return redirect('/listings/'+listing_id)