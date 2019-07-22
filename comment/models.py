from django.db import models
from board.models import Board

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content