from app.models import db, Payment, Loan

def record_payment(loan_id, amount_paid, payment_type):
    """
    Record a payment for a loan and update the balance.
    """
    loan = Loan.query.get(loan_id)
    if loan:
        # Calculate new balance
        new_balance = loan.principal_amount - amount_paid
        payment = Payment(
            loan_id=loan_id,
            amount_paid=amount_paid,
            payment_type=payment_type,
            balance_remaining=new_balance
        )
        loan.principal_amount = new_balance
        db.session.add(payment)
        db.session.commit()
        return payment
    return None