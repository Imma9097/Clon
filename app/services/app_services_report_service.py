from app.models import db, Client, Loan, Payment
from flask import jsonify

def generate_daily_report():
    """
    Generate a report for all transactions made today.
    """
    from datetime import datetime, date
    today = date.today()
    payments = Payment.query.filter(db.func.date(Payment.payment_date) == today).all()
    report = {
        'date': today.strftime('%Y-%m-%d'),
        'total_payments': len(payments),
        'payments': [
            {
                'loan_id': payment.loan_id,
                'amount_paid': payment.amount_paid,
                'payment_type': payment.payment_type,
                'balance_remaining': payment.balance_remaining
            } for payment in payments
        ]
    }
    return jsonify(report)