from flask import Blueprint, request, jsonify
from app.models import db, Client, Loan, Payment

# Blueprint for routes
main = Blueprint('main', __name__)

# Route to add a new client
@main.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    client = Client(
        name=data['name'],
        id_number=data['id_number'],
        mobile_number=data['mobile_number'],
        residence=data['residence'],
        business_type=data['business_type'],
        business_location=data['business_location']
    )
    db.session.add(client)
    db.session.commit()
    return jsonify({'message': 'Client added successfully!'}), 201

# Route to issue a loan
@main.route('/loans', methods=['POST'])
def issue_loan():
    data = request.get_json()
    loan = Loan(
        client_id=data['client_id'],
        principal_amount=data['principal_amount'],
        weekly_installment=data['weekly_installment']
    )
    db.session.add(loan)
    db.session.commit()
    return jsonify({'message': 'Loan issued successfully!'}), 201

# Route to make a payment
@main.route('/payments', methods=['POST'])
def make_payment():
    data = request.get_json()
    payment = Payment(
        loan_id=data['loan_id'],
        amount_paid=data['amount_paid'],
        payment_type=data['payment_type'],
        balance_remaining=data['balance_remaining']
    )
    db.session.add(payment)
    db.session.commit()
    return jsonify({'message': 'Payment recorded successfully!'}), 201