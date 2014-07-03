# -*- coding: utf-8 -*-

#crudgenerator auto-generated code.
#crudgenetaror date: 3rd July 2014 02:22


from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Contact


__all__ = ('ContactListView', 'ContactUpdateView',
           'ContactCreateView', 'ContactDeleteView')


class ContactListView(ListView):
    model = Contact
    paginate_by = 20


class ContactDeleteView(DeleteView):
    model = Contact

    def get_success_url(self):
        return reverse("contacts:contact:list", args=(1,))


class ContactCreateView(CreateView):
    model = Contact

    def get_success_url(self):
        return reverse("contacts:contact:list", args=(1,))


class ContactUpdateView(UpdateView):
    model = Contact

    def get_success_url(self):
        return reverse("contacts:contact:list", args=(1,))
