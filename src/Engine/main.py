from calculate_total_cost import get_total_calc

costs = {
    'Coffee': {'type': 'float', 'value': 2.50},
    'Service Charge': {'type': 'percent', 'value': 0.05},
    'VAT': {'type': 'percent', 'value': 0.20}
}

discounts = {
    'Eat Out to Help Out': {'type': 'percent', 'value': 0.50}
}

subtotal, total_discount, grand_total = get_total_calc(costs, discounts)

print("\nSubtotal", subtotal)
print("\nTotal Discount", total_discount)
print("\nGrand Total", grand_total)
