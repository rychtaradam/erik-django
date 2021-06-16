from django.shortcuts import render
from series.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    num_serials = Serial.objects.all().count()
    serials = Serial.objects.order_by('-rate')[:3]

    context = {
        'num_serials': num_serials,
        'serials': serials
    }

    return render(request, 'index.html', context=context)


class SerialListView(generic.ListView):
    model = Serial
    context_object_name = "serial_list"
    paginate_by = 10


class SerialDetailView(generic.DetailView):
    model = Serial
    context_object_name = "serial"


class DirectorListView(generic.ListView):
    model = Director
    context_object_name = "director_list"
    paginate_by = 10


class GenresListView(generic.ListView):
    model = Genre
    context_object_name = "genre_list"
    paginate_by = 10


class SerialCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Serial
    fields = ['name', 'genre', 'director', 'date', 'series', 'rate']
    permission_required = 'series.can_add_serials'

    def get_success_url(self):
        return reverse_lazy('series')


class SerialUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Serial
    fields = '__all__'
    permission_required = 'series.can_update_serials'


class SerialDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Serial
    success_url = reverse_lazy('series')
    permission_required = 'series.can_delete_serials'


class GenreCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Genre
    fields = ['name']
    permission_required = 'series.can_add_genres'

    def get_success_url(self):
        return reverse_lazy('genres')


class GenreUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    permission_required = 'series.can_update_genres'


class GenreDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy('genres')
    permission_required = 'series.can_delete_genres'


class DirectorCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Director
    fields = ['name']
    permission_required = 'series.can_add_directors'

    def get_success_url(self):
        return reverse_lazy('directors')


class DirectorUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Director
    fields = '__all__'
    permission_required = 'series.can_update_directors'


class DirectorDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Director
    success_url = reverse_lazy('directors')
    permission_required = 'series.can_delete_directors'
