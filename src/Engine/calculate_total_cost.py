def get_total_calc(costs, discounts):
    subtotal = 0
    total_discount = 0
    grand_total = 0
    float = 0

    # Calculate subtotal
    for cost in costs:
        if costs[cost]['type'] == 'percent':
            percent = costs[cost]['value']
            percent += 1
            float = percentage_to_value(percent, subtotal)
            subtotal += float
        elif costs[cost]['type'] == 'float':
            float = costs[cost]['value']
            subtotal += float

    # Calculate total discount
    for discount in discounts:
        if discounts[discount]['type'] == 'percent':
            percent = discounts[discount]['value']
            float = percentage_to_value(percent, subtotal)
            total_discount += float
        elif discounts[discount]['type'] == 'float':
            float = discounts[discount]['value']
            total_discount += float

    grand_total = subtotal - total_discount

    return subtotal, total_discount, grand_total


def percentage_to_value(percent, original_value):
    return original_value * percent
