from django.forms import ModelForm
from base.models import TODO


class TODOForms(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']
