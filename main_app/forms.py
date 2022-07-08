
from django.forms import ModelForm
from .models import Bloom

class BloomForm(ModelForm):
  class Meta:
    model = Bloom
    fields = ['date', 'bloom']