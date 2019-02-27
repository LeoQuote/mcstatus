from django.test import TestCase, Client
from mc.models import Server
from unittest.mock import patch
from django.utils import timezone
from datetime import timedelta
# Create your tests here.


class ServerTest(TestCase):
    def setUp(self):
        self.s1 = Server(name='test', description='some_test',directory='/home/work/some_dir')
        self.s1.save()
        self.s2 = Server(name='test2', description='some_test', directory='some_dire', status='ok',
                         last_checked_at=timezone.now() - timedelta(minutes=6))
        self.s2.save()

    def tearDown(self):
        self.s1.delete()

    @patch('mc.models.check_server')
    def testSuccessServer(self, _check):
        _check.return_value = 'ok'
        check_result = self.s1.get_status()
        self.assertEqual('ok', check_result)
        check_result = self.s2.get_status()
        self.assertEqual('ok', check_result)

    @patch('mc.models.check_server')
    def testFailedServer(self, _check):
        _check.return_value = 'not ok'
        check_result = self.s1.get_status()
        self.assertEqual('not ok', check_result)
        check_result = self.s2.get_status()
        self.assertEqual('not ok', check_result)


class StatusViewTest(TestCase):

    def setUp(self):
        self.s1 = Server(name='test', description='some_test', directory='/home/work/some_dir', status='ok',
                         last_checked_at=timezone.now())
        self.s1.save()

    def tearDown(self):
        self.s1.delete()

    def test_status_view(self):
        c = Client()
        r = c.get('/')
        self.assertTemplateUsed(r, 'status.html')
        self.assertContains(r, self.s1.name)
