"""
Unittests for obs.views
"""
from opal.core.test import OpalTestCase
from unittest.mock import MagicMock

from obs import views

class ObsChartViewTestCase(OpalTestCase):
    def test_get_context_data(self):
        self.patient, self.episode = self.new_patient_and_episode_please()
        view = views.ObsChartView()
        ctx = view.get_context_data(episode_id=self.episode.id)
        self.assertEqual(ctx['episode'].id, self.episode.id)
