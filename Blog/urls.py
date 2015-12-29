from django.conf.urls import patterns, include, url
from django.contrib import admin

from article.views import ArticleListView, ArticleDetailView, AddComment

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Bla.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ArticleListView.as_view()),
    url(r'^(?P<slug>[-\w]+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^comment/add/$', AddComment.as_view(), name='comment_add'),
)
