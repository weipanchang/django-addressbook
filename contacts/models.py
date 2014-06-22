from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255,)
    last_name = models.CharField(max_length=255,)
    email = models.EmailField()
#    def __unicode__(self):  # Python 3: def __str__(self):
#        return self.question

    def __str__(self):
        return ' '.join([self.first_name, self.last_name,])