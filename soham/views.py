from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')

def certifications(request):
    return render(request,'certifications.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Optional: Save to DB or send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Example email sending (optional)
            send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message}",
                email,  # From email
                ['youremail@example.com'],  # To email
            )
            return render(request, 'contact.html')  # You can create a "thank_you.html" page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
