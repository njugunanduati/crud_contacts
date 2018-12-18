from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact


class ContactList(ListView):
    model = Contact
    template_name  = 'contacts/contact_list.html'


class ContactDetail(DetailView):
    model = Contact
    template_name = 'contacts/contact_details.html'


class ContactCreate(CreateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = ['name', 'email', 'address', 'phone']
    success_url = reverse_lazy('contact_list')


class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'contacts/contact_form.html'
    fields = ['name', 'email', 'address', 'phone']
    success_url = reverse_lazy('contact_list')


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'
