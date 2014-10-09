# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from zbx_dashboard.models import Board
from django.utils import translation


def create_board(title, description):
    return Board.objects.create(
        title=title,
        description=description
    )


class BoardViewTests(TestCase):    # pylint: disable=R0904

    def setUp(self):
        """
        Initialize test user and login him
        """
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(
            self.username, self.email, self.password)
        self.client.login(
            username=self.username, password=self.password)
        translation.activate('en')

    def test_index_view_with_n_boards(self):
        response = self.client.get(reverse('boards:list'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'No dashboards')
        self.assertQuerysetEqual(response.context['object_list'], [])
