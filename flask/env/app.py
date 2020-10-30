from flask import Flask, render_template
import config, csv
from binance.client import Client

app =Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)

@app.route('/')
def index():
    title ='Coinview'
    info =client.get_account()
    print(info)
    return render_template ('index.html', title=title)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'
