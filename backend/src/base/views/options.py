from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView,
    DeleteView, ListView
)

from ..models import Options


class OptionsCreateView(CreateView):
    model = Options
    template_name = 'options_edit.html'
    fields = ['name', 'value']

    def get_success_url(self):
        return reverse_lazy('options-list')


class OptionsListView(ListView):
    template_name = 'options_list.html'
    model = Options


class OptionsUpdateView(UpdateView):
    model = Options
    template_name = 'options_edit.html'
    fields = ['name', 'value']

    def get_success_url(self):
        return reverse_lazy('options-list')


class OptionsDeleteView(DeleteView):
    model = Options
    success_url = reverse_lazy('options-list')
    template_name = 'options_confirm_delete.html'
