from django.views.generic import ListView
from .models import Articles
# Create your views here.


class ArticleView(ListView):
    model = Articles
    template_name = "article_list.html"