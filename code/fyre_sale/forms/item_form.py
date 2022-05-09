from django.forms import ModelForm, widgets
from items.models import ItemForSale

class CandyCreateItem(ModelForm):
    class Meta:
        model = ItemForSale
        exclude = ['id', 'cur_bid']
        widgets = {
            'name' : widgets.TextInput(attrs='eitthvað sniðugt')
        }