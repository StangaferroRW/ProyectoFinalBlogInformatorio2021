from django.contrib import admin
from .models import Post, Comentario, Categoria
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'contenido', 'fecha_creacion', 'categoria',)
	list_filter = ('titulo', 'fecha_creacion','categoria', 'comentario')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
admin.site.register(Categoria)