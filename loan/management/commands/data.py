from django.core.management.base import BaseCommand

from loan.management.data import data_for_load
from loan.models import Contract, CreditApplication, Manufacturer, Product, CreditApplicationProduct


class Command(BaseCommand):
    """ Класс для загрузки основных параметров проекта в БД """

    def handle(self, *args, **options):

        if Contract.objects.count() == 0:
            contracts = [Contract(**item) for item in data_for_load.contracts]
            Contract.objects.bulk_create(contracts)

        if CreditApplication.objects.count() == 0:
            credit_applications = [CreditApplication(**item) for item in data_for_load.loans]
            CreditApplication.objects.bulk_create(credit_applications)

        if Manufacturer.objects.count() == 0:
            manufacturers = [Manufacturer(**item) for item in data_for_load.manufacturers]
            Manufacturer.objects.bulk_create(manufacturers)

        if Product.objects.count() == 0:
            products = [Product(**item) for item in data_for_load.products]
            Product.objects.bulk_create(products)

        if CreditApplicationProduct.objects.count() == 0:
            application_products = [CreditApplicationProduct(**item) for item in data_for_load.application_products]
            CreditApplicationProduct.objects.bulk_create(application_products)
