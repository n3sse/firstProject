from django.views.generic import TemplateView, DetailView, ListView
from .models import Post, Author


class HomePageView(TemplateView):
    """ HomePageView as the name says,
    it returns a view for index page.
    It contains three newest Posts
    and authors which are making this page."""
    template_name = "blog_page/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['recent_post'] = Post.objects.all()[:3]
        context['authors'] = Author.objects.all()
        return context


class BlogPageView(ListView):
    """ BlogPageView returns a view for all
        Posts which this site contains. """
    model = Post
    template_name = "blog_page/blog_page.html"
    context_object_name = "post_list"
    paginate_by = 6


class PostDetailView(DetailView):
    """ PostDetailView is a view which returns
        full model of single Post. """
    model = Post
    template_name = "blog_page/detail_page.html"
