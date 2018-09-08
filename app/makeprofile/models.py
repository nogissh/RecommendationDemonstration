from django.db import models


class UserProfile(models.Model):
  code = models.CharField(null=True, max_length=200)
  name = models.CharField(null=False, max_length=200)
  q1 = models.IntegerField(null=False, default=99)
  q2 = models.IntegerField(null=False, default=99)
  q3 = models.IntegerField(null=False, default=99)
  q4 = models.IntegerField(null=False, default=99)
  q5 = models.IntegerField(null=False, default=99)
  enabled = models.BooleanField(default=False)
  def __str__(self):
    return f'{self.name}'
