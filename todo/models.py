from django.db import models

class ToDo(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=140)
    
    def __str__(self):
        return self.content