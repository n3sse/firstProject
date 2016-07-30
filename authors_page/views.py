from django.shortcuts import render
from django.views.generic import TemplateView
from blog_page.models import Author


class HomePageView(TemplateView):

    template_name = "authors_page/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        context['authors'] = Author.objects.all()
        return context


