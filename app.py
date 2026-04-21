from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

carrito = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        producto = request.form['producto']
        carrito.append(producto)
        return redirect(url_for('index'))

    return render_template('index.html', carrito=carrito)

if __name__ == '__main__':
    app.run(debug=True)