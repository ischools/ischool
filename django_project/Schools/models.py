from django.db import models

def resume_upload_dir(instance, filename):
    return 'resumes/{0}'.format(filename)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

class Resume(models.Model):
    applicant_name  = models.CharField(max_length=100, blank=True, null=True)
    applicant_email = models.CharField(max_length=1000, blank=True, null=True)
    about_applicant = models.CharField(max_length=1000, blank=True, null=True)
    why_to_join  = models.CharField(max_length=200, blank=True, null=True) 
    resume_file = models.FileField(upload_to = resume_upload_dir,
                                blank=True, null=True)
    class Meta:
        verbose_name = 'resumes'