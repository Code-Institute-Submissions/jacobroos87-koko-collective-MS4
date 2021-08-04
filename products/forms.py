from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductImage


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'sku', 'name', 'description', 'has_sizes', 'price', 'avg_rating', 'is_featured', 'main_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['main_image'].required = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ImageForm(ProductForm):

    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(ProductForm.Meta):
        fields = ProductForm.Meta.fields + ['images',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].required = False
