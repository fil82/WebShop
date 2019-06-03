from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ProfileUser
# Create your views here.


def redirect_user(request):
    # url = f'/'
    url = f'/shop/'

    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'
