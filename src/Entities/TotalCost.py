class TotalCost:
    costs = {
        'Item Costs': {'type': 'float', 'values': [2.99, 4.50, 1.60, 6.70, 3.00]},
        'Service Charge': {'type': 'percent', 'value': 0.10},
        'VAT': {'type': 'percent', 'value': 0.20}
    }

    discounts = {
        'Eat Out to Help Out': {'type': 'percent', 'value': 0.50}
    }

    def __init__(self, costs, discounts):
        self.costs = costs
        self.discounts = discounts

    def get_costs(self):
        return self.costs

    def get_discounts(self):
        return self.discounts

