from django.db import models


class MemoModel(models.Model):
    title = models.CharField(max_length=100)
    key = models.CharField(max_length=20)
    code = models.TextField()
    degree = models.TextField()
    
    def __str__(self):
        return self.title