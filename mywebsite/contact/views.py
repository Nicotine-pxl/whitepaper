from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            language = form.cleaned_data['language']
            message = form.cleaned_data['message']

            send_mail(
                f'New Message from {name} ({language})',
                message,
                'your-email@example.com',
                ['your-email@example.com'],
                fail_silently=False,
            )
            return render(request, 'contact/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
