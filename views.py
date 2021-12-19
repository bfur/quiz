from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from itnet.mixins.navMixin import navMixin
from itnet.views import ItnetCreateView, ItnetDeleteView, ItnetDetailView, ItnetListView, ItnetUpdateView, ItnetViewSettings

quizSidebar = [

]

class QuizViewSettings(ItnetViewSettings):
    def __init__(self, sidebar=quizSidebar):
        super().__init__(sidebar=sidebar)

class indexView(LoginRequiredMixin, View, navMixin):
    def get(self, request, sidebar = None):
        sidebar = sidebar if sidebar != None else quizSidebar
        
        return render(request, "home.html", {'sidebar': navMixin.get_sidebar(request,sidebar), 'navbar': navMixin.get_navbar(request), 'source': 'you are at quiz'})

class QuizlistView(ItnetListView):
    def __init__(self, view_settings_class=None, model=None):
        if view_settings_class == None:
            view_settings_class = QuizViewSettings()  
        super().__init__(view_settings_class=view_settings_class, model=model)

class QuizDetailView(ItnetDetailView):
    pass 

class QuizCreateView(ItnetCreateView):
    pass

class QuizUpdateView(ItnetUpdateView):
    pass

class QuizDeleteView(ItnetDeleteView):
    pass