from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from spidey_rest.models import GizmodoEntry
from spidey_rest.serializers import GizmodoEntrySerializer
from spidey_rest.serializers import GizmodoEntryMetaSerializer
from django.db import transaction


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
        # Sort by descending post_id value
        g_entries = GizmodoEntry.objects.order_by('-post_id')
        g_serializer = GizmodoEntryMetaSerializer(g_entries, many=True)
        transaction.commit()
        return HttpResponse(g_serializer.data)


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

