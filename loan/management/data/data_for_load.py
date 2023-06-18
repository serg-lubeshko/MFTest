contracts = [
    {"id": 1,
     "name": "Contract 1",
     },
    {"id": 2,
     "name": "Contract 2"
     }
]

loans = [
    {
        "id": 1,
        "name": "Loan Application #1-F",
        "contract_id": 1
    },
    {
        "id": 2,
        "name": "Loan Application #2A-F",
        "contract_id": 2
    }
]

manufacturers = [
    {
        "pk": 1,
        "name": "Apple"
    },
    {
        "pk": 2,
        "name": "Nike"
    },
    {
        "pk": 3,
        "name": "Samsung"
    },
    {
        "pk": 4,
        "name": "BMW"
    }
]

products = [
    {
        "pk": 1,
        "name": "S20",
        "manufacturer_id": 3
    },
    {
        "pk": 2,
        "name": "S21",
        "manufacturer_id": 3
    },
    {
        "pk": 3,
        "name": "S22",
        "manufacturer_id": 3
    },
    {
        "pk": 4,
        "name": "iPhone 14",
        "manufacturer_id": 1
    },
    {
        "pk": 5,
        "name": "iPhone 15",
        "manufacturer_id": 1
    }
]

application_products = [
    {
        "pk": 1,
        "credit_application_id": 1,
        "product_id": 1
    },
    {
        "pk": 2,
        "credit_application_id": 2,
        "product_id": 2
    },
    {
        "pk": 3,
        "credit_application_id": 1,
        "product_id": 3
    },
    {
        "pk": 4,
        "credit_application_id": 1,
        "product_id": 4
    },
    {
        "pk": 5,
        "credit_application_id": 1,
        "product_id": 5
    }
]
