from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductImage


# Adding a product form
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'sku', 'name', 'description',
                  'has_sizes', 'price', 'avg_rating',
                  'is_featured', 'main_image']

    main_image = forms.ImageField(label='Main Image',
                                  required=True,
                                  widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


# Form to handle extra images
class ImageForm(ProductForm):

    class Meta(ProductForm.Meta):
        fields = ProductForm.Meta.fields + ['images',]

    images = forms.FileField(
        label='Extra Images', required=False,
        widget=CustomClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
