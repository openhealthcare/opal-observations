"""
Plugin definition
"""
from opal.utils import OpalPlugin

from obs import urls

class ObservationsPlugin(OpalPlugin):
    """
    Plugin for obs
    """
    urls = urls.urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/obs/controllers/obs_chart.js'
        ]
    }
