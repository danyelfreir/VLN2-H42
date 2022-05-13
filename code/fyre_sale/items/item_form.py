from django import forms
from items.models import ItemForSale, SubCategory, Offer, ItemImages
from django.forms import ModelForm, widgets

CONDITIONS = {
    ('Refurbished', 'Refurbished'),
    ('Used - Like new', 'Used - Like new'),
    ('Used', 'Used'),
    ('For spare parts', 'For spare parts'),
}


class CreateItem(ModelForm):

    class Meta:
        model = ItemForSale
        fields = '__all__'
        widgets = {
            'condition':
            widgets.Select(attrs={'class': 'form-field'}, choices=CONDITIONS),
        }

    def __init__(self, *args, **kwargs):
        super(CreateItem, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'


class GetImages(ModelForm):

    class Meta:
        model = ItemImages
        fields = '__all__'
        widgets = {
            'image':
            widgets.FileInput(
                attrs={
                    'class': 'form-field',
                    'enctype': 'multipart/form-data',
                    'multiple': True
                }),
        }

    def __init__(self, *args, **kwargs):
        super(GetImages, self).__init__(*args, **kwargs)
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
            raise forms.ValidationError(
                u"Your bid must be higher than the current bid.")
        return self.cleaned_data


class EditAd(ModelForm):

    class Meta:
        model = ItemForSale
        fields = '__all__'

        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-field'}),
            'condition': widgets.Select(attrs={'class': 'form-field'}, choices=CONDITIONS),
            'long_desc': widgets.Textarea(attrs={'class': 'form-field'}),
        }

    def __init__(self, item=None, *args, **kwargs):
        self.item = item
        super(EditAd, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'