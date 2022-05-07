from django.db import models


class CreateNewsletter(models.Model):
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.subject
