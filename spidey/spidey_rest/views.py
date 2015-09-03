from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from spidey_rest.models import GizmodoEntry
from spidey_rest.serializers import GizmodoEntrySerializer
# Create your views here.

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
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        g_entries = GizmodoEntry.objects.all()
        g_serializer = GizmodoEntrySerializer(g_entries, many=True)
        return JSONResponse(g_serializer.data)


