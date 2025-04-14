from datetime import datetime, timedelta

def check_defaulter_status(payment_date, today=None):
    """
    Determine the defaulter status based on payment arrears.
    """
    if today is None:
        today = datetime.now()
    
    days_in_arrears = (today - payment_date).days
    if days_in_arrears <= 7:
        return 'Yellow'  # First week arrears
    elif 8 <= days_in_arrears <= 14:
        return 'Green'  # Second week arrears
    elif days_in_arrears > 14:
        return 'Red'  # Third week arrears
    return 'None'