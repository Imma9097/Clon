from app.models import db, Loan

def calculate_weekly_installment(principal, interest_rate):
    """
    Calculate the weekly installment based on the principal and interest rate.
    """
    return principal * (interest_rate / 100)

def apply_penalty(loan_id, penalty_rate):
    """
    Apply a penalty to the weekly installment if the payment is overdue.
    """
    loan = Loan.query.get(loan_id)
    if loan:
        penalty = loan.weekly_installment * (penalty_rate / 100)
        loan.weekly_installment += penalty
        db.session.commit()
        return loan.weekly_installment
    return None