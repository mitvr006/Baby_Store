from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Send an email (Optional)
        send_mail(
            subject=f"Contact Form Submission from {name}",
            message=f"Message: {message}\n\nFrom: {email}",
            from_email='your_email@example.com',  # Replace with your email
            recipient_list=['admin@example.com'],  # Replace with admin's email
            fail_silently=False,
        )

        return HttpResponse("Thank you for contacting us!")

    return render(request, "pages/contact.html")
