from flask import Flask, request, render_template, redirect, flash, session
from currency import Currency

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something-secret'



@app.route('/')
def show_form():
    return render_template('form.html')

@app.route('/validate', methods=['GET', 'POST'])
def validate_data():
    res = request.form
    c = Currency(res)
    check = c.validate_input()
    
    if len(check) == 3:
        session['converted-price'] = c.get_conversion()
        return redirect('/convert')
    else:
        session['converted-price'] = ''

        if res['convert-from'].upper() not in check: 
            flash(f'Invalid or missing code to convert from: {res["convert-from"]}') 

        if res['convert-to'].upper() not in check: 
            flash(f'Invalid or missing code to convert to: {res["convert-to"]}')

        if res['amount'] not in check: 
            flash(f'Invalid or missing amount: {res["amount"]}')
        
        
        return redirect('/')
    
    return redirect('/')

@app.route('/convert')
def show_converted():
    if 'converted-price' not in session.keys():
        return redirect('/')
    return render_template('convert.html', converted_price=session['converted-price'])






      

        
       
            
            

    


