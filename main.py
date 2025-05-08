from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = 'aqui_e_a_minha_chave'

contatos = []

@app.route('/')
def index():
    return render_template( 'index.html', contatos = contatos)
@app.route('/adicionar_contato', methods = ['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        codigo = len(contatos)
        contatos.append([codigo, nome, telefone, email])
        flash('Contato cadastrado com sucesso!!')

        return redirect('/')
    else:
        return render_template('adicionar_contato.html')

@app.route( '/editar_contato/<int:codigo>', methods=['GET','POST'])
def editar_contato(codigo):
    if request.method =='POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        contatos[codigo] = [codigo, nome, telefone, email]
        flash('Contato editado com sucesso!!')
        return redirect('/')
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato = contato)

@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    del contatos[codigo]
    flash('Contato excluido com sucesso!!')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
