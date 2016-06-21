from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Paste
from .forms import PasteForm

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def home(request):
    form = PasteForm(request.POST or None)
    code = Paste.objects.last()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(code.id + 1)
    
    return render(request, 'home.html', {'form': form, 'code': code})


def codeView(request, id):
    code = Paste.objects.get(pk=id)
    lexer = get_lexer_by_name(code.language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass=code.style)
    result = highlight(code.new_paste, lexer, formatter)
    return render(request, 'code-view.html', {"code": code, "result": result})
