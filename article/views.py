from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Article, Comment
from .forms import CommentForm

# Create your views here.

class ArticleListView(ListView):
	model = Article
	context_object_name = 'articles_list'
	template_name = 'articles_list.html'

class ArticleDetailView(DetailView):
	model = Article
	context_object_name = 'article'
	template_name = 'article_detail.html'

	def get_context_data(self, **kwargs):
		context = super(ArticleDetailView, self).get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(comment_article=self.object)
		context['comment_form'] = CommentForm(initial={'comment_article': self.object})
		return context

class AddComment(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'article_detail.html'
	http_method_names = ['post']