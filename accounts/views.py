from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


@login_required(login_url='login')
def Profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    return render(request, 'profile.html', {'user': user})


class EditProfile(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')  # Replace 'profile' with the URL name of your profile view

    def get_object(self, queryset=None):
        # This method is used to fetch the specific user's profile to edit
        # We want to make sure the currently logged-in user is editing their own profile
        return self.request.user
