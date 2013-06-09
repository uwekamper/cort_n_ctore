from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Place', blank=True, null=True, related_name="children")
    type = models.CharField(max_length=255)

    def __unicode__(self):
        result = ''
        if self.parent:
            result = self.parent.__unicode__() + '>'

        result += '%s: %s' % (self.type, self.name)
        return result


class Part(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place)
    general_type = models.CharField(max_length=255, blank=True, null=True)
    specific_type = models.CharField(max_length=255, blank=True, null=True)
    from_value = models.FloatField(blank=True, null=True)
    to_value = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=255, default='', blank=True, null=True)
    package = models.CharField(max_length=255, blank=True, null=True)

    note = models.TextField(blank=True, null=True)
    remaining = models.CharField(null=True, blank=True, max_length=255)

    def __unicode__(self):
        return self.name


