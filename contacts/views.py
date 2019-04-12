from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made this inquiry ')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id,)
        contact.save()

        # Send_mail
        '''send_mail(
            #'Property Listing Inquiry',
            #'There has been an inquiry for' +listing +'Sing into the admin panel for more info',
            #'someemail@gmail.com',
            #[realor_email, 'techguyinfo@gmail.com'],
            #fail_silently=False
        )'''

        messages.success(request, 'Your request has been submitted, a realtor will call you out soon! ')
        return redirect('/listings/'+listing_id)




