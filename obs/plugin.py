"""
Plugin definition
"""
from opal.core import plugins

from obs import urls

class ObservationsPlugin(plugins.OpalPlugin):
    """
    Plugin for obs
    """
    urls = urls.urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/obs/controllers/obs_chart.js',
            'js/obs/services/records/observation.js',
        ]
    }
