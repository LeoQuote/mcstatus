from django.db import models
from datetime import timedelta
from django.utils import timezone
from mc.utils import check_server, start_server
# Create your models here.


class Server(models.Model):
    name = models.CharField('服务器名字', max_length=32)
    description = models.CharField('服务器描述', max_length=256)
    directory = models.CharField('服务器目录', max_length=256)
    status = models.CharField('服务器状态', max_length=32, default='unknown')
    last_checked_at = models.DateTimeField(null=True, blank=True)
    last_started_at = models.DateTimeField(null=True, blank=True)

    def get_status(self):
        if self.status == 'unknown' or \
                self.last_checked_at is None or self.last_checked_at < timezone.now() - timedelta(minutes=5):
            self.status = check_server(self.directory)
            self.last_checked_at = timezone.now()
            super().save()
        return self.status

    def start_server(self):
        if self.status == 'ok':
            return 'ok'
        else:
            start_server(self.directory)
            return 'ok'