"""
Unittests for obs.views
"""
from opal.core.test import OpalTestCase
from django.core.urlresolvers import reverse

from obs import views


class ObsChartViewTestCase(OpalTestCase):
    def test_get_context_data(self):
        self.patient, self.episode = self.new_patient_and_episode_please()
        view = views.ObsChartView()
        ctx = view.get_context_data(episode_id=self.episode.id)
        self.assertEqual(ctx['episode'].id, self.episode.id)

    def test_get(self):
        self.patient, self.episode = self.new_patient_and_episode_please()
        url = reverse('obs_chart', kwargs=dict(episode_id=self.episode.id))
        self.assertTrue(
            self.client.login(
                username=self.user.username, password=self.PASSWORD
            )
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
