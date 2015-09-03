from rest_framework import serializers
from spidey_rest.models import GizmodoEntry

class GizmodoEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GizmodoEntry
        fields = ('id', 'title', 'author', 'post_id', 'created', 'text')