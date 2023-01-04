from django.conf import settings
from django.db import models
from django.urls import reverse


class ProductType(models.Model):

    name = models.CharField(verbose_name=_("Product Name"), help_text=_(
        "Required"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/default.png')
    price = models.DecimalField(decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
