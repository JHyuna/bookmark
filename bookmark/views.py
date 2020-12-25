from django.shortcuts import render

from django.views.generic.list import ListView
from .models import Bookmark

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

# templates 폴더의 base.html에 {paginate} 부분이 먼저 있어야됨 (페이징 기능)
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5