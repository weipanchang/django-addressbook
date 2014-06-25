from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from django.views.generic import ListView
#from django.views.generic import QueryView

from contacts.models import Contact

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    
    def get_success_url(self):
        return reverse('contacts-list')
    
class CreateQueryView(ListView):
    model = Contact
    template_name = 'query_contact.html'
    Contact.objects.raw('SELECT * FROM contacts WHERE last_name = %s', ['chang'])
    def get_success_url(self):
        return reverse('contacts-list')

# Create your views here.
