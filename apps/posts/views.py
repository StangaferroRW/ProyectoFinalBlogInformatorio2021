from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarPosts(LoginRequiredMixin, ListView):
	model = Post
	template_name = "postsList.html"
	context_object_name = "posts"
	#def get_queryset(self):
	#	noticias = Noticia.objects.all().order_by('-fecha_creacion')
	#	return noticias


class DetallePosts(LoginRequiredMixin, DetailView):
	model = Post
	template_name = "postsDetail.html"
