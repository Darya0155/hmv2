from django.forms import ModelForm

from addons.models import Addon


class AddonForm(ModelForm):
    class Meta:
        model = Addon
        fields = '__all__'
        exclude = ('hotel',"deleted_at")