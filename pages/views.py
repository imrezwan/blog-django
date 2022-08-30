from django.views.generic import TemplateView, ListView
from pages.models import Post

# def homePageView(request):
#     return HttpResponse('Hello World')

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name: str = 'aboutus.html'
