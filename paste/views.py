from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
# Create your views here.
from .models import Paste
from .forms import PasteForm

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def home(request):
    pastes = Paste.objects.all().order_by('-id')[:5]
    form = PasteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.id)
    return render(request, 'home.html', {'form': form, 'pastes': pastes})


def codeView(request, id):
    code = get_object_or_404(Paste, pk=id)
    lexer = get_lexer_by_name(code.language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass=code.style)
    result = highlight(code.new_paste, lexer, formatter)
    return render(request, 'code-view.html', {"code": code, "result": result})
