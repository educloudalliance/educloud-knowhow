from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class QuestionTests(APITestCase):
    def test_list_feature_requests(self):
        """
        Ensure we can list 10 latest feature requests.
        """
        url = reverse('question-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
