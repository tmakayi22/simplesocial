from django.views.generic import TemplateView

# Create Login view`
class TestPage(TemplateView):
    template_name = 'test.html'


# Create Logout view
class ThanksPage(TemplateView):
    template_name = 'thanks.html'


# Create Home page view
class HomePage(TemplateView):
    template_name = 'index.html'
