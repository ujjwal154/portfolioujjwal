from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_msg = f"name:{name} \n Email : {email}\n Subject : {subject} \n Message : {message} "
        print(full_msg)
        send_mail(subject=subject ,message=full_msg, from_email=email, recipient_list=['udhiman001@gmail.com'],)
        messages.success(request, 'your email is sent')
        return redirect('home')

    return render(request, "index.html")

def projects(request):
    return render(request, 'project.html')


