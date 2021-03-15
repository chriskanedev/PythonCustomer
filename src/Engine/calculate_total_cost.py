def get_total_calc(costs, discounts):
    subtotal = float(0)
    total_discount = float(0)
    grand_total = float(0)

    # Calculate subtotal
    subtotal = sum(costs['Item Costs']['values'])

    # Calculate total discount
    for discount in discounts:
        if discounts[discount]['type'] is 'percent':
            percent = discounts[discount]['value']
        elif discounts[discount]['type'] is 'float':
            float = discounts[discount]['value']

    return subtotal, total_discount, grand_total

