from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from spidey_rest.models import GizmodoEntry
from spidey_rest.serializers import GizmodoEntrySerializer
from collections import OrderedDict


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def spidey_main(request):
    """
    List meta (title, author, keywords, description) for all posts, starting with more recent one
    """
    if request.method == 'GET':
        data = []
        l = 'title', 'author', 'url', 'post_id', 'post_date', 'keywords', 'description'
        ge = GizmodoEntry.objects.values(*l).order_by('-post_id')
        # This is awful; reordering the output of '.values' (with random ordering) according to l
        for g in ge:
            data.append(OrderedDict((k, g[k]) for k in l))
        return JSONResponse(data)


def spidey_full_post(request, post_id):
    """
    Show full info (title, author, keywords, description, full text) for a single post
    """
    try:
        g_entry = GizmodoEntry.objects.get(post_id=post_id)
    except GizmodoEntry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        g_serializer = GizmodoEntrySerializer(g_entry)
        return JSONResponse(g_serializer.data)

