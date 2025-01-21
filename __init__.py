from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('jeu_de_des.html')

@app.route('/jack')
def exo_jack():
     return render_template('jack.svg')
  
@app.route('/jeu_de_des_amelioration')
def exo_de():
     return render_template('jeu_de_des_amelioration.html')

@app.route('/bibliotheque_images')
def exo_bibliotheque_images():
     return render_template('bibliotheque_images.html')
  
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
