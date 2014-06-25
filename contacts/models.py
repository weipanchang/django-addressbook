from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255,)
    last_name = models.CharField(max_length=255,)
    email = models.EmailField()
#    def __unicode__(self):  # Python 3: def __str__(self):
#        return self.question

    def __str__(self):
        return ' '.join([self.last_name, ', ', self.first_name,])
    
    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Contact._meta.fields]
    
    def query_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Contact._meta.fields if self.last_name == 'chang']