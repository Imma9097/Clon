from app import db
from datetime import datetime

# Client Model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(20), nullable=False, unique=True)
    mobile_number = db.Column(db.String(15), nullable=False)
    residence = db.Column(db.String(100), nullable=False)
    business_type = db.Column(db.String(50), nullable=False)
    business_location = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Loan Model
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    principal_amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, default=8.0)
    appraisal_fee = db.Column(db.Float, default=300.0)
    weekly_installment = db.Column(db.Float, nullable=False)
    penalty_rate = db.Column(db.Float, default=10.0)
    status = db.Column(db.String(20), default="Active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Payment Model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'), nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    payment_type = db.Column(db.String(20), nullable=False)
    balance_remaining = db.Column(db.Float, nullable=False)

# Report Model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(20), nullable=False)
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    report_data = db.Column(db.Text)