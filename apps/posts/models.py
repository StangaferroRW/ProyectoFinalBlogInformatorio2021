from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):

	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name =("Post")
		verbose_name_plural =("Posts")
