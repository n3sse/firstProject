from django.views.generic import ListView
from .models import Post
# Create your views here.


class ListPosts(ListView):
    model = Post
    context_object_name = "posts_list"
    template_name = "blog_page/index.html"

    def get_context_data(self, **kwargs):
        context = super(ListPosts, self).get_context_data(**kwargs)
        return context

