from django.views.generic import TemplateView #1

class HomePageView(TemplateView): #2
    template_name = 'home.html'

class AboutPageView(TemplateView): # 3
    template_name = 'about.html'   
