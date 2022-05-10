from django.forms import ModelForm, widgets
from django import forms
from items.models import ItemForSale, SubCategory, Offer


# class CreateItem(forms.Form):
#     CONDITION_CHOICES = [
#         ('new', 'New'),
#         ('for parts or repair', 'For parts or repair'),
#         ('used - like new', 'Used - Like new'),
#         ('used - decent', 'Used - Decent'),
#         ('refurbished', 'Refurbished'),
#         ('refurbished - certified', 'Refurbished - Certified')
#     ]
#     SUBCAT_CHOICES = []
#     subcats = SubCategory.objects.all().order_by('name')
#     for i, sc in enumerate(subcats, start=1):
#         SUBCAT_CHOICES.append((i, sc.name))
#
#     name = forms.CharField(required=True, max_length=255)
#     image = forms.URLField(required=False)
#     min_bid = forms.IntegerField(required=True)
#     long_desc = forms.CharField(required=True, max_length=9999)
#     sub_cat_id = forms.ChoiceField(required=True, widget=forms.Select, choices=SUBCAT_CHOICES)
#     condition = forms.ChoiceField(required=True, widget=forms.Select, choices=CONDITION_CHOICES)
#     date_of_upload = forms.CharField(required=False, max_length=255)
#     time_of_upload = forms.CharField(required=False, max_length=255)
#     sold = forms.BooleanField(required=False)
#     seller_id = forms.IntegerField(required=False)
#
#     def __init__(self, *args, **kwargs):
#         super(CreateItem, self).__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             field.field.widget.attrs['class'] = 'form-field'



#
# class CreateItem(ModelForm):
#      class Meta:
#          conditions = [('new', 'New'),
#                        ('for parts or repair','For parts or repair'),
#                        ('used - like new', 'Used - Like new'),
#                        ('used - decent', 'Used - Decent'),
#                        ('refurbished', 'Refurbished'),
#                        ('refurbished - certified', 'Refurbished - Certified')
#                        ]
#          model = ItemForSale
#          exclude = ['id']
#          widgets = {
#             'seller': widgets.NumberInput(),
#             'name': widgets.TextInput(attrs={'class': 'form-field'}),
#             'image': widgets.FileInput(attrs={'class': 'form-field'}),
#             'condition': widgets.Select(attrs={'class': 'form-field'}, choices=conditions),
#             'min_bid': widgets.NumberInput(attrs={'class': 'form-field'}),
#             'long_desc': widgets.Textarea(attrs={'class': 'form-field'}),
#             'sub_cat': widgets.Select(attrs={'class': 'form-field'})
#          }


class CreateItem(ModelForm):
    class Meta:
        model = ItemForSale
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CreateItem, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'

class PlaceBid(ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(PlaceBid, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-field'
