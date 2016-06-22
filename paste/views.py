from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Paste
from .forms import PasteForm, LoginForm

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def home(request):
    current_user = request.user
    if request.user.is_authenticated():
        loggedIn = True
    else:
        loggedIn = False
    print (current_user, loggedIn)
    pastes = Paste.objects.all().order_by('-id')[:5]
    form = PasteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.id)
    context = {
        'form': form,
        'pastes': pastes,
        'current_user': current_user,
        'loggedIn': loggedIn
    }
    return render(request, 'home.html', context)


def codeView(request, id):
    code = get_object_or_404(Paste, pk=id)
    lexer = get_lexer_by_name(code.language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass=code.style)
    result = highlight(code.new_paste, lexer, formatter)
    context = {
        "code": code, "result": result,

    }
    return render(request, 'code-view.html', context)

def userLogin(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                raise "Contact to Author!!"
        else:
            raise "Sorry You are Wrong!!"

    return render(request, 'login.html', {"form": form})