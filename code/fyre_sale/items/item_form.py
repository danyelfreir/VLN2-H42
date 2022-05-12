from django import forms
from items.models import ItemForSale, SubCategory, Offer
from django.forms import ModelForm, widgets

class CreateItem(ModelForm):
    class Meta:
        model = ItemForSale
        fields = '__all__'
        conditions = {
            ('Refurbished', 'Refurbished'),
            ('Used - Like new', 'Used - Like new'),
            ('Used', 'Used'),
            ('For spare parts', 'For spare parts'),
        }
        widgets = {
            'condition': widgets.Select(attrs={'class': 'form-field'}, choices=conditions),
            'image': widgets.FileInput(attrs={'class': 'form-field', 'enctype': 'multipart/form-data', 'multiple': True}),
        }
    def __init__(self, *args, **kwargs):
        super(CreateItem, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'


class PlaceBid(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'

    def __init__(self, item=None, *args, **kwargs):
        self.item = item
        super(PlaceBid, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'

    def clean(self):
        price = self.cleaned_data['price']
        if price < self.item.cur_bid:
            raise forms.ValidationError(u"Your bid must be higher than the current bid.")
        return self.cleaned_data
