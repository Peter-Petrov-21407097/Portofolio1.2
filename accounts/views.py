from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .forms import MagicLinkForm

def login_view(request):
    erro = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('portfolio:index')
        else:
            erro = 'Username ou password inválidos.'

    return render(request, 'accounts/login.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return redirect('portfolio:index')


def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio:index')
    else:
        form = RegistoForm()

    return render(request, 'accounts/registo.html', {'form': form})