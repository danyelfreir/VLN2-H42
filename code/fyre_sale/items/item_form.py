from django.forms import ModelForm, widgets
from items.models import ItemForSale






# class CreateItem(ModelForm):
#      class Meta:
#          conditions = [('new', 'New'),
#                        ('for parts or repair','For parts or repair'),
#                        ('used - like new', 'Used - Like new'),
#                        ('used - decent', 'Used - Decent'),
#                        ('refurbished', 'Refurbished')
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

    def save(self, commit=True):
        itemforsale = super(CreateItem, self).save(commit=False)
        if commit:
            itemforsale.save()
        return itemforsale