from unittest import TestCase
from app import app
from currency import Currency
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, session 

class ConverterTestCase(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_homepage(self):
        with self.client:
            response = self.client.get('/')
            html = response.get_data(as_text=True)

            self.assertIn('<form action="/validate" method="post">', html)

    def test_converter(self):
        with self.client as client:
            response = client.post('/validate', data = {'convert-from': 'usd', 'convert-to': 'usd', 'amount': 1})

            self.assertEqual(session['converted-price'], '$ 1.0')

    def test_redirect_convert(self):
        response = self.client.get('/convert')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')
