"""
Views for the Opal observations plugin
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ObsChartView(LoginRequiredMixin, TemplateView):
    """
    Render an obs chart for this episode.
    """
    template_name = 'obs/chart.html'

    def get_context_data(self, *a, **kw):
        from opal.models import Episode

        ctx = super(ObsChartView, self).get_context_data(*a, **kw)
        ctx['episode'] = Episode.objects.get(pk=kw['episode_id'])
        return ctx
