from django.views.generic import TemplateView, View
from .models import Post


class BlogPageView(TemplateView):

    template_name = "blog_page/index.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        context['recent_post'] = Post.objects.latest('post_date')
        return context
