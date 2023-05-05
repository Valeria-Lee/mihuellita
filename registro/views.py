from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import CreateUser
from .models import Usuario
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def acerca(request):
    return render(request, 'acerca.html')

def consejos(request):
    return render(request, 'consejos.html')

def articulo1(request):
    return render(request, 'articulos/art1.html')

def articulo2(request):
    return render(request, 'articulos/art2.html')

def articulo3(request):
    return render(request, 'articulos/art3.html')

def art_chable(request):
    return render(request, 'articulos/art_chable.html')

def estadisticas(request):
    return render(request, 'estadisticas.html')

mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
    'api_key': settings.MAILCHIMP_API_KEY,
    'server': settings.MAILCHIMP_REGION,
})

def registrar(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            errors = []

            # validar si el usuario ya existe.
            if Usuario.objects.filter(username=username).exists():
                errors.append('El nombre de usuario ya existe') # se añade el error a la lista.

            # validar si el correo ya existe.
            if Usuario.objects.filter(email=email).exists():
                errors.append('El correo electrónico ya existe') # se añade el error a la lista.

            if errors:
                # agregar los errores a la lista de errores del formulario
                for error in errors:
                    form.add_error(None, error) # agrega un error al formulario asociado a un campo específico o a un campo no específico.
                    # los errores de validación están asociados a campos específicos del formulario. 
                return render(request, 'user/registro.html', {'form': form})
            else:
                # si no existen, se renderiza la página de user creado.
                Usuario.objects.create(username=username, email=email)
                mensaje = render_to_string('./confirmacion.html', {'username':username})
                mail = EmailMessage(
                    'MiHuellita: Confirmación de registro', # subject
                    mensaje, # message
                    settings.EMAIL_HOST_USER, # from email
                    [email], # to email
                )
                mail.fail_silently=False
                mail.send()
                member_info = {
                    'email_address': email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                return render(request, 'user/user_creado.html')
    else:
        form = CreateUser()
    return render(request, 'user/registro.html', {'form': form})