from flask import Flask, render_template, request, redirect, url_for, flash
from bank import Bank
from account import Account, SavingAccount, CurrentAccount

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Create a global bank instance
bank = Bank()

@app.route('/')
def index():
    return render_template('index.html', accounts=bank.accounts)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        holder_name = request.form.get('holder_name')
        acc_type = request.form.get('acc_type')
        
        if not holder_name or not acc_type:
            flash('All fields are required!', 'error')
            return redirect(url_for('create_account'))
        
        acc_number = bank.create_account(holder_name, acc_type)
        flash(f'Account created successfully! Account Number: {acc_number}', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_account.html')

@app.route('/account/<acc_number>')
def account_details(acc_number):
    acc = bank.find_account(acc_number)
    if not acc:
        flash('Account not found!', 'error')
        return redirect(url_for('index'))
    return render_template('account.html', account=acc)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        acc_number = request.form.get('acc_number')
        amount = request.form.get('amount')
        
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Amount must be positive!', 'error')
                return redirect(url_for('deposit'))
            
            acc = bank.find_account(acc_number)
            if not acc:
                flash('Account not found!', 'error')
                return redirect(url_for('deposit'))
            
            acc.deposit(amount)
            flash(f'Deposited ₹{amount} successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid amount!', 'error')
            return redirect(url_for('deposit'))
    
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        acc_number = request.form.get('acc_number')
        amount = request.form.get('amount')
        
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Amount must be positive!', 'error')
                return redirect(url_for('withdraw'))
            
            acc = bank.find_account(acc_number)
            if not acc:
                flash('Account not found!', 'error')
                return redirect(url_for('withdraw'))
            
            acc.withdraw(amount)
            flash(f'Withdrew ₹{amount} successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid amount!', 'error')
            return redirect(url_for('withdraw'))
    
    return render_template('withdraw.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        from_acc = request.form.get('from_acc')
        to_acc = request.form.get('to_acc')
        amount = request.form.get('amount')
        
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Amount must be positive!', 'error')
                return redirect(url_for('transfer'))
            
            from_account = bank.find_account(from_acc)
            to_account = bank.find_account(to_acc)
            
            if not from_account or not to_account:
                flash('One or both accounts not found!', 'error')
                return redirect(url_for('transfer'))
            
            if from_account.get_balance() < amount:
                flash('Insufficient funds!', 'error')
                return redirect(url_for('transfer'))
            
            bank.transfer(from_acc, to_acc, amount)
            flash(f'Transferred ₹{amount} successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid amount!', 'error')
            return redirect(url_for('transfer'))
    
    return render_template('transfer.html')

@app.route('/transactions/<acc_number>')
def transactions(acc_number):
    acc = bank.find_account(acc_number)
    if not acc:
        flash('Account not found!', 'error')
        return redirect(url_for('index'))
    
    transactions = acc.get_transaction_history()
    return render_template('transactions.html', account=acc, transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)