from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomeUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)

class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
