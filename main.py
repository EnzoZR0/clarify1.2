import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
  return 'Melhor site daqui'

@app.route('/total/')
def total():
  tabela = pd.read_csv('base.csv')
  total_vendas = tabela ['Vendas'].sum()
  resposta = {'Total Vendas:': total_vendas}
  return jsonify (resposta)

@app.route('/media/')
def media():
  tabela = pd.read_csv('base.csv')
  media_vendas = tabela ['Vendas'].mean()
  resposta = {'Media Vendas:': media_vendas}
  return jsonify (resposta)

@app.route('/composto/')
def composto():
  tabela = pd.read_csv('base.csv')
  media_vendas = tabela ['Vendas'].mean()
  total_vendas = tabela ['Vendas'].sum()
  resposta = {'Media Vendas:': media_vendas, 'Total Vendas:': total_vendas}
  return jsonify(resposta)

if __name__ == "__main__":
  app.run('0.0.0.0')


  
  
