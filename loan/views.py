import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MFT.settings")

import django

django.setup()
from django.db.models import Subquery, QuerySet
from loan.models import Product, Manufacturer, CreditApplication


def get_unigue_manufacturer(contract_id: int) -> QuerySet[int]:
    """
    :param contract_id: int
    :return: QuerySet[int]

    Реализовал 2 способа получения уникальных id производителей товаров:

    1. способ через property модели
    2. функция get_unigue_manufacturer
    """

    credit_application_id = CreditApplication.objects.get(contract_id=contract_id).id
    unique_manufactures = Manufacturer.objects.filter(
        id__in=Subquery(
            Product.objects.filter(product_applications__credit_application_id=credit_application_id).values(
                'manufacturer_id'))
    ).values_list("id", flat=True)
    return unique_manufactures


if __name__ == '__main__':
    contract_id = 1
    print(get_unigue_manufacturer(contract_id))

    manufactures_id = CreditApplication.objects.get(contract_id=contract_id)
    print(manufactures_id.unigue_manufacturers)
