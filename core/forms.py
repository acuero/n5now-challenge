from django.contrib.auth.forms import UserCreationForm
from core.models.oficial import Oficial


class OficialCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

    class Meta:
        model = Oficial
        fields = ('password1', 'password2')
