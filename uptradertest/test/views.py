from django.shortcuts import render
from django.views.generic import DetailView

from .models import MenuItem

def test(request):
    return render(request, 'test/index.html')


class GetMenuItem(DetailView):
    model = MenuItem
    template_name = 'test/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        return context