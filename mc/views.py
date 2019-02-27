from django.shortcuts import render
from mc.models import Server
# Create your views here.


def statusView(request):
    servers = Server.objects.all()
    servers_info = []
    for s in servers:
        s.get_status()
        servers_info += [s]
    return render(request, 'status.html', context={'servers':servers_info})
