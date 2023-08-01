from django.db import models  
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_pdf_upload(value):
    user_email = "sudarshan15399@gmail.com"
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        raise ValidationError("You are not authorized to upload PDF files.")


def pdf_upload_path(instance, filename):
    # Customize the upload path and filename as per your requirement
    return f'pdfs/{filename}'

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    pdf_file = models.FileField(upload_to=pdf_upload_path, validators=[validate_pdf_upload])
    author = models.CharField(max_length=30, default='Guest')
    email = models.EmailField(blank=True)
    description = models.TextField(default='Available in Library')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.picture:
            self.picture.name = f'pictures/{self.picture.name}'
        super().save(*args, **kwargs)    
