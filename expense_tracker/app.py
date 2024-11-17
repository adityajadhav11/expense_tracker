from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Dataframe to store expenses
expenses_df = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    date = request.form['date']
    category = request.form['category']
    amount = float(request.form['amount'])

    new_expense = {'Date': date, 'Category': category, 'Amount': amount}
    global expenses_df
    expenses_df = expenses_df.append(new_expense, ignore_index=True)

    return render_template('success.html')

@app.route('/view_expenses')
def view_expenses():
    return render_template('expenses.html', expenses=expenses_df.to_html())

if __name__ == '__main__':
    app.run(debug=True)