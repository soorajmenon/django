import django.views.generic

# Create your views here.class Home(TemplateView):
class Home(django.views.generic.TemplateView):
     template_name='index.html'

# Create your views here.
