from django.shortcuts import render

# Create your views here.
from .models import Paste

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def home(request):
    code = Paste.objects.last()
    lexer = get_lexer_by_name(code.language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass=code.style)
    result = highlight(code.new_paste, lexer, formatter)
    return render(request, 'home.html', {"code": code, "result": result})
