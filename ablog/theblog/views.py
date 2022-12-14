from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import post, Category, Comment
from . forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#from django.contrib.auth.models.

from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
#def home(request):
	#return render(request, 'home.html', {})

def LikeView(request, pk):
	p = get_object_or_404(post, id=pk)
	liked = False
	if p.likes.filter(id=request.user.id).exists():
		p.likes.remove(request.user)
		liked = False
	else:
		p.likes.add(request.user)
		liked = True
	context = {
		'post': p,
		'liked': liked,
	}
	return render(request, 'article_details.html', context)

#@login_required
class HomeView(ListView):
	model = post
	template_name = 'home.html'
	ordering = ['-post_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		#context = {}
		#user = self.request.user
		#if user.is_authenticated:

		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'category_list.html':cat_menu_list})


def CategoryView(request, cats):
	category_posts = post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})


class ArticleDetailView(DetailView):
	model = post
	template_name = 'article_details.html'
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		
		stuff = get_object_or_404(post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title', 'body')

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	#fields = ('name', 'body')
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = ('title', 'body')

class UpdatePostView(UpdateView):
	model = post
	template_name = 'update_post.html'
	form_class = EditForm
	#fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')


