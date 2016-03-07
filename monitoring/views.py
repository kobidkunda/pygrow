from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


# def index(request):
#     return HttpResponse('PyGrow dashboard view')

# def index(request):
#     return render(request, '_base.html')

class IndexView(TemplateView):
    """
    View for all monitoring.
    """
    template_name = '_base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page_title'] = 'PyGrow'

        return context


class SettingsView(TemplateView):
    """
    View for monitoring settings.
    """
    template_name = 'settings.html'

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context['page_title'] = 'PyGrow'

        return context


class CameraView(TemplateView):
    """
    View for Camera monitoring.
    """
    template_name = 'camera.html'

    def get_context_data(self, **kwargs):
        context = super(CameraView, self).get_context_data(**kwargs)
        context['page_title'] = 'PyGrow Camera'

        return context


class TemperatureView(TemplateView):
    """
    View for Temperature monitoring.
    """
    template_name = 'temperature.html'

    def get_context_data(self, **kwargs):
        context = super(TemperatureView, self).get_context_data(**kwargs)
        context['page_title'] = 'PyGrow Temperature'

        return context


class HumidityView(TemplateView):
    """
    View for Humidity monitoring.
    """
    template_name = 'humidity.html'

    def get_context_data(self, **kwargs):
        context = super(HumidityView, self).get_context_data(**kwargs)
        context['page_title'] = 'PyGrow Humidity'

        return context
