from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from Schools.models import Resume
from django.core.mail import send_mail
from django.conf import settings
  
def ia_home(request):
    if request.method=="POST":
        applicant_name  = request.POST.get('name')
        applicant_email = request.POST.get('email')
        about_applicant = request.POST.get('about_applicant')
        why_to_join     = request.POST.get('why_to_join')
        # resume_file     = request.FILES[0]
        print(applicant_name, applicant_email, about_applicant, why_to_join)
        new_resume      = Resume()
        new_resume.applicant_name  = applicant_name
        new_resume.applicant_email = applicant_email
        new_resume.about_applicant = about_applicant
        new_resume.why_to_join     = why_to_join
        exists = Resume.objects.all().filter(applicant_email=applicant_email)
        if not exists:
            new_resume.save()    
            from_email = [settings.EMAIL_HOST_USER]
            to_email  = [applicant_email]
            subject = 'Welcome in Imperial Arkon'
            message_to_user = 'Hey '+ applicant_name+'!\n'\
                            + 'We are happy that you are interested in joining team IA. I am sure that this is going to '\
                            + 'be really exciting.\n'\
                            + 'We will be back to you soon.\n'\
                            + 'bbyee!\n'\
                            + 'Team IA, www.imperialarkon.hohos.in'
            send_mail(subject, message_to_user, from_email, to_email, fail_silently=False)
            print('after saving')
            status = 'true'
        else: status='false'
        return render(request, 'ia/ia_home.html',{'status':status})
    else:
        return render(request, 'ia/ia_home.html', {})

def ia_apply(request):
    return HttpResponse('success')
