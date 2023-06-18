from django.db import models
from django.db.models import Subquery


class ModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    name = models.CharField(max_length=255, verbose_name="Наименование")

    class Meta:
        abstract = True

    def __str__(self):
        return f"id{self.id}: {self.name}"


class CreditApplication(ModelMixin):
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "кредитная заявка"
        verbose_name_plural = "Кредитные заявки"

    @property
    def unigue_manufacturers(self):
        unique_manufactures = Manufacturer.objects.filter(
            id__in=Subquery(
                Product.objects.filter(product_applications__credit_application_id=self.id).values(
                    'manufacturer_id'))
        ).values_list("id", flat=True)
        return unique_manufactures


class Contract(ModelMixin):
    class Meta:
        verbose_name = "контракт"
        verbose_name_plural = "Контракты"


class Product(ModelMixin):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


class Manufacturer(ModelMixin):
    class Meta:
        verbose_name = "производитель"
        verbose_name_plural = "Производители"


class CreditApplicationProduct(models.Model):
    credit_application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        error_messages={"unique": "Товар уже связан с заявкой"},
        related_name='product_applications'
    )

    class Meta:
        unique_together = ("product",)
