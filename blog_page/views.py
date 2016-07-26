from django.views.generic import TemplateView, DetailView
from .models import Post


class HomePageView(TemplateView):

    template_name = "blog_page/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['recent_post'] = Post.objects.all()[:3]
        # context['thumbnail_loop'] = range(1, 4)
        return context


class BlogPageView(TemplateView):

    template_name = "blog_page/blog_page.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog_page/detail_page.html"
