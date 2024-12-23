# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"Name: {name}, Email: {email}, Message: {message}")

            send_mail(
                f"Message from {name}",
                message,
                email,
                ['recipient@example.com'],  # Replace with your email
            )
            
            # Return a success message
            return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})



