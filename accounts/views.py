from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .forms import MagicLinkForm
from django.contrib.auth.models import Group

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)

        if form.is_valid():
            user = form.save()

            grupo_autores, created = Group.objects.get_or_create(name="autores")
            user.groups.add(grupo_autores)

            login(request, user)
            return redirect('home')
    else:
        form = RegistoForm()

    return render(request, 'accounts/registo.html', {'form': form})

def magic_link_request_view(request):
    mensagem = None

    if request.method == "POST":
        form = MagicLinkForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            try:
                user = User.objects.get(email=email)

                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                magic_url = request.build_absolute_uri(
                    reverse("accounts:magic_login", kwargs={
                        "uidb64": uid,
                        "token": token
                    })
                )

                send_mail(
                    "Link mágico de login",
                    f"Clica neste link para entrar no portfólio:\n\n{magic_url}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

            except User.DoesNotExist:
                pass

            mensagem = "Se o email existir, foi enviado um link mágico."
    else:
        form = MagicLinkForm()

    return render(request, "accounts/magic_link.html", {
        "form": form,
        "mensagem": mensagem
    })


def magic_login_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        login(request, user)
        return redirect("home")

    return render(request, "accounts/magic_link_invalid.html")

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