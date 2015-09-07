from rest_framework import serializers
from spidey_rest.models import GizmodoEntry


class GizmodoEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GizmodoEntry
        fields = ('id',
                  'created',
                  'title',
                  'author',
                  'url',
                  'post_id',
                  'post_date',
                  'keywords',
                  'description',
                  'text'
                  )


class GizmodoEntryMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GizmodoEntry
        fields = ('id',
                  'created',
                  'title',
                  'author',
                  'url',
                  'post_id',
                  'post_date',
                  'keywords',
                  'description'
                  )
