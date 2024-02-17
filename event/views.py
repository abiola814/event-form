from django.shortcuts import render, redirect
from .forms import EventAttendeeForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt  # Add this import


def index(request):
    context = {'name': 'Your Name'} 
    return render(request, 'index.html', context)


@csrf_exempt
def event_attendee_view(request):
    if request.method == 'POST':
        form = EventAttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved info")
            return render(request, 'index.html', {'message': "Thank you for registering"})  # Replace 'success_page' with your success page URL

    return render(request, 'index.html', {'message': "try again"})


def event_attendee_view(request):
    email_sent = False

    if request.method == 'POST':
        form = EventAttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save()

            # Send email with HTML template
            subject = 'Thank you for registering'
            message = f'Thank you for registering for the event! Your unique ID is: {attendee.unique_id}'
            from_email = 'yakubayatoo@gmail.com'  # Replace with your email address
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True, html_message=get_html_template(attendee))

            email_sent = True
            print(attendee.unique_id)
            # Redirect or perform other actions after successful form submission
            return render(request, 'index.html', {'message': "Thank you for registering"})  # Replace 'success_page' with your success page URL
    else:
        form = EventAttendeeForm()

    return render(request, 'index.html', {'message': "try again"})

def get_html_template(attendee):
    # You can customize the HTML template for the email here
    html_template = f"""
        <html>
        <body>
            <p>Thank you for registering for the event!</p>
            <p>Your unique ID is: {attendee.unique_id}</p>
            <!-- Add more HTML content as needed -->
        </body>
        </html>
    """
    return html_template