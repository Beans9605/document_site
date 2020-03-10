from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def write_email(request) :
    return render (request, 'email_function/email_write.html')

def email_send(request) :
    email = request.POST.get('email')
    title = request.POST.get('title')
    content = request.POST.get('content')

    content = content + " "  + email

    send_mail(
        "[멋쟁이사자처럼 문의내용] " + title,         # 제목
        content, # 내용
        email,     # 보내는 이메일  (settings에 설정해서 작성안해도 됨)
        ['alkad1234@likelion.org'],     # 받는 이메일 리스트
        fail_silently=False,
    )

    return redirect('home')