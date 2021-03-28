from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import TypeForm

import string

class PercentageView(TemplateView):
    template_name = ""
    form = TypeForm()
    context = {
        'judul': 'Percentage Char Function',
        'content': 'Percentage Function',
        'banner': 'percentage/img/banner_about.png',
        'app_css': 'percentage/css/style.css',
        'form': form,
        'result': ''
    }


    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.method == 'POST':
            self.context['type_alfabet'] = request.POST['type_alfabet']
            self.context['sentence'] = request.POST['sentence']

            if self.context['type_alfabet'].strip() == "":
                return 0

            count = sum([1 if char in self.context['sentence'] else 0 for char in self.context['type_alfabet']])
            spaces = self.context['type_alfabet'].count(" ")
            total_chars = len(self.context['type_alfabet']) - spaces

            self.context['result'] = round((count / total_chars) * 100, 3)
        return render(request, self.template_name, self.context)