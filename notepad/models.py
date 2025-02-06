from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User model is already created and linked.  # This is a foreign key field which links to the User model.
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']


    def __sef__(self):
        return self.title

# Create your models here.
