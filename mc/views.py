from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from mc.models import Server
# Create your views here.


def statusView(request):
    servers = Server.objects.all()
    servers_info = []
    for s in servers:
        s.get_status()
        servers_info += [s]
    return render(request, 'status.html', context={'servers':servers_info})


def startView(request, server_id):
    mc_server = get_object_or_404(Server, pk=server_id)
    if mc_server.status == 'ok':
        return HttpResponseBadRequest('搞事情呢小老弟？服务器已经ok了。')
    start_result = mc_server.start_server()
    return HttpResponse(start_result)