from django.db import models
from django.db import IntegrityError


class GizmodoEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    text = models.TextField(default='')
    description = models.TextField(default='')
    keywords = models.TextField(default='')
    post_id = models.CharField(max_length=50, unique=True)
    post_date = models.CharField(max_length=50, default='')
    url = models.CharField(max_length=500, default='')

    class Meta:
        ordering = ('created',)

    def save(self):
        try:
            #self.save()
            models.Model.save(self)
        except IntegrityError as e:
            #return render_to_response("template.html", {"message": e.message})
            print "Save error: " + e.message
