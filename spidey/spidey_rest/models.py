from django.db import models
from django.db import IntegrityError
from django.shortcuts import render_to_response


class GizmodoEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    text = models.TextField()
    post_id = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('created',)

    def save(self):
        try:
            #self.save()
            models.Model.save(self)
        except IntegrityError as e:
            #return render_to_response("template.html", {"message": e.message})
            print "Save error: " + e.message
