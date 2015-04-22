"""
Views for the OPAL observations plugin
"""
from django.views.generic import TemplateView

from opal.models import Episode
from opal.core.views import LoginRequiredMixin

class ObsChartView(LoginRequiredMixin, TemplateView):
    """
    Render an obs chart for this episode.
    """
    template_name = 'obs/chart.html'

    def get_context_data(self, *a, **kw):
        ctx = super(ObsChartView, self).get_context_data(*a, **kw)
        ctx['episode'] = Episode.objects.get(pk=kw['episode_id'])
        return ctx

