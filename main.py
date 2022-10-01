from flask import Flask, render_template, request
from model import model
import this

this.nome = ""
this.apelido = ""
this.nSUS = ""
this.rg = ""
this.cpf = ""
this.mae = ""
this.data = ""
this.sexo = ""
this.municipioN = ""
this.nacionalidade = ""
this.paisN = ""
this.alfa = ""
this.escolaridade = ""
this.raca = ""
this.religiao = ""
this.ocupacao = ""
this.conjugal = ""
this.ubs = ""
this.alergia = ""
this.deficiencia = ""
this.qualD = ""
this.sangue = ""
this.fator = ""
this.rua = ""
this.num = ""
this.complemento = ""
this.bairro = ""
this.ref = ""
this.cep = ""
this.municipioE = ""
this.estado = ""
this.telefone = ""
this.celular = ""
this.email = ""
this.pergunta1 = ""
this.pergunta2 = ""
this.pergunta3 = ""
this.pergunta4 = ""
this.pergunta5 = ""
this.pergunta6 = ""
this.pergunta7 = ""
this.pergunta8 = ""
this.pergunta9 = ""
this.pergunta10 = ""
this.pergunta11 = ""
this.pergunta12 = ""
this.refNome = ""
this.refNascimento = ""
this.refVinculo = ""
this.refEndereco = ""
this.refTel = ""
this.refMora = ""
this.refDataInfo = ""
this.dados = ""
this.modelo = model()
this.codigo = 0
this.msg = ""
this.campo = ""
this.dado = ""
this.dia = ""
this.hora = ""
this.descricao = ""
this.duvida = ""
this.ajuda = ""
this.altura = ""
this.diabetes = ""
this.dieta = ""
this.peso = ""
this.pressao = ""

idoso = Flask(__name__)

@idoso.route('/', methods=['GET','POST'])
def inicio():
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)

#---------------cadastrar---------------#

@idoso.route('/cadastrar.html', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        #-------------Informações do idoso-------------#
        this.nome          = request.form['tNovoNome']
        this.apelido       = request.form['tNovoApelido']
        this.nSUS          = request.form['tNovoNSUS']
        this.rg            = request.form['tNovoRG']
        this.cpf           = request.form['tNovoCPF']
        this.mae           = request.form['tNovoMae']
        this.data          = request.form['tNovaData']
        this.sexo          = request.form['tNovoSexo']
        this.municipioN    = request.form['tNovoMunicipioN']
        this.nacionalidade = request.form['tNovaNacionalidade']
        this.paisN         = request.form['tNovoPaisN']
        this.alfa          = request.form['tNovoAlfa']
        this.escolaridade  = request.form['tNovaEscolaridade']
        this.raca          = request.form['tNovaRaca']
        this.religiao      = request.form['tNovaReligiao']
        this.ocupacao      = request.form['tNovaOcupacao']
        this.conjugal      = request.form['tNovoConjugal']
        this.ubs           = request.form['tNovaUBS']
        this.alergia       = request.form['tNovaAlergia']
        this.deficiencia   = request.form['tNovaDeficiencia']
        this.qualD         = request.form['tNovoQualD']
        this.sangue        = request.form['tNovoSangue']
        this.fator         = request.form['tNovoFator']
        #-------------Endereço Residencial-------------#
        this.rua         = request.form['tNovaRua']
        this.num         = request.form['tNovoNum']
        this.complemento = request.form['tNovoComplemento']
        this.bairro      = request.form['tNovoBairro']
        this.ref         = request.form['tNovaRef']
        this.cep         = request.form['tNovoCEP']
        this.municipioE  = request.form['tNovoMunicipioE']
        this.estado      = request.form['tNovoEstado']
        this.telefone    = request.form['tNovoTelefone']
        this.celular     = request.form['tNovoCelular']
        this.email       = request.form['tNovoEmail']
        #-------------Informações sociofamiliares-------------#
        this.pergunta1  = request.form['tNovaPergunta1']
        this.pergunta2  = request.form['tNovaPergunta2']
        this.pergunta3  = request.form['tNovaPergunta3']
        this.pergunta4  = request.form['tNovaPergunta4']
        this.pergunta5  = request.form['tNovaPergunta5']
        this.pergunta6  = request.form['tNovaPergunta6']
        this.pergunta7  = request.form['tNovaPergunta7']
        this.pergunta8  = request.form['tNovaPergunta8']
        this.pergunta9  = request.form['tNovaPergunta9']
        this.pergunta10 = request.form['tNovaPergunta10']
        this.pergunta11 = request.form['tNovaPergunta11']
        this.pergunta12 = request.form['tNovaPergunta12']
        #-------------Pessoas de referência-------------#
        this.refNome       = request.form['tNovaRefNome']
        this.refNascimento = request.form['tNovaRefNascimento']
        this.refVinculo    = request.form['tNovaRefVinculo']
        this.refEndereco   = request.form['tNovaRefEndereco']
        this.refTel        = request.form['tNovaRefTel']
        this.refMora       = request.form['tNovaRefMora']
        this.refDataInfo   = request.form['tNovaRefDataInfo']
        #-------------------------------------------------#
        this.dados = this.modelo.inserirIdoso(this.nome, this.apelido, this.nSUS, this.rg, this.cpf, this.mae, this.data, this.sexo, this.municipioN, this.nacionalidade, this.paisN, this.alfa, this.escolaridade, this.raca, this.religiao, this.ocupacao, this.conjugal, this.ubs, this.alergia, this.deficiencia, this.qualD, this.sangue, this.fator, this.rua, this.num, this.complemento, this.bairro, this.ref, this.cep, this.municipioE, this.estado, this.telefone, this.celular, this.email, this.pergunta1, this.pergunta2, this.pergunta3, this.pergunta4, this.pergunta5, this.pergunta6, this.pergunta7, this.pergunta8, this.pergunta9, this.pergunta10, this.pergunta11, this.pergunta12, this.refNome, this.refNascimento, this.refVinculo, this.refEndereco, this.refTel, this.refMora,  this.refDataInfo)
    return render_template('cadastrar.html', titulo="Cadastro Idoso", resultado=this.dados)

@idoso.route('/cadastrarConsulta.html', methods=['GET','POST'])
def consultaCadastrar():
    if request.method == 'GET':
        this.msg = this.modelo.consultarIdoso()
    return render_template('cadastrarConsulta.html', titulo="Consultar Dados Idoso", dados=this.msg)

@idoso.route('/cadastrarAtualiza.html', methods=['GET','POST'])
def atualizaCadastrar():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarIdoso(this.codigo, this.campo, this.dado)
    return render_template('cadastrarAtualiza.html', titulo="Atualizar Dados Idoso", dados=this.msg)

@idoso.route('/cadastrarExclui.html', methods=['GET','POST'])
def excluiCadastrar():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirIdoso(this.codigo)
    return render_template('cadastrarExclui.html', titulo="Excluir Dados Idoso", dados=this.msg)
    
#---------------cadastrar---------------#

#---------------agenda---------------#

@idoso.route('/agenda.html', methods=['GET','POST'])
def agenda():
    if request.method == 'POST':
        this.dia       = request.form['tNovaAgendaData']
        this.hora      = request.form['tNovaAgendaHora']
        this.descricao = request.form['tNovaAgendaDesc']
        this.msg = this.modelo.inserirAgenda(this.dia, this.hora, this.descricao)
    return render_template('agenda.html', titulo="Agenda", dados=this.msg)

@idoso.route('/agendaConsulta.html', methods=['GET','POST'])
def consultaAgenda():
    if request.method == 'GET':
        this.msg = this.modelo.consultarAgenda()
    return render_template('agendaConsulta.html', titulo="Consultar Agenda", dados=this.msg)

@idoso.route('/agendaAtualiza.html', methods=['GET','POST'])
def atualizaAgenda():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarAgenda(this.codigo, this.campo, this.dado)
    return render_template('agendaAtualiza.html', titulo="Atualizar Agenda", dados=this.msg)

@idoso.route('/agendaExclui.html', methods=['GET','POST'])
def excluiAgenda():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirAgenda(this.codigo)
    return render_template('agendaExclui.html', titulo="Excluir Agenda", dados=this.msg)

#---------------agenda---------------#

#---------------ajuda---------------#    

@idoso.route('/ajuda.html', methods=['GET','POST'])
def ajuda():
    if request.method == 'POST':
        this.duvida = request.form['tNovaAjudaDuvida']
        this.ajuda  = request.form['tNovaAjudaAjuda']
        this.msg = this.modelo.inserirAjuda(this.duvida, this.ajuda)
    return render_template('ajuda.html', titulo="Ajuda", dados=this.msg)

@idoso.route('/ajudaConsulta.html', methods=['GET','POST'])
def consultaAjuda():
    if request.method == 'GET':
        this.msg = this.modelo.consultarAjuda()
    return render_template('ajudaConsulta.html', titulo="Consultar Ajuda", dados=this.msg)

@idoso.route('/ajudaAtualiza.html', methods=['GET','POST'])
def atualizaAjuda():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarAjuda(this.codigo, this.campo, this.dado)
    return render_template('ajudaAtualiza.html', titulo="Atualizar Ajuda", dados=this.msg)

@idoso.route('/ajudaExclui.html', methods=['GET','POST'])
def excluiAjuda():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirAjuda(this.codigo)
    return render_template('ajudaExclui.html', titulo="Excluir Ajuda", dados=this.msg)

#---------------ajuda---------------#

#---------------altura---------------#
    
@idoso.route('/altura.html', methods=['GET','POST'])
def altura():
    if request.method == 'POST':
        this.dia       = request.form['tNovaAlturaData']
        this.hora      = request.form['tNovaAlturaHora']
        this.altura = request.form['tNovaAlturaAltura']
        this.msg = this.modelo.inserirAltura(this.dia, this.hora, this.altura)
    return render_template('altura.html', titulo="Altura", dados=this.msg)

@idoso.route('/alturaConsulta.html', methods=['GET','POST'])
def consultaAltura():
    if request.method == 'GET':
        this.msg = this.modelo.consultarAltura()
    return render_template('alturaConsulta.html', titulo="Consultar Altura", dados=this.msg)

@idoso.route('/alturaAtualiza.html', methods=['GET','POST'])
def atualizaAltura():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarAltura(this.codigo, this.campo, this.dado)
    return render_template('alturaAtualiza.html', titulo="Atualizar Altura", dados=this.msg)

@idoso.route('/alturaExclui.html', methods=['GET','POST'])
def excluiAltura():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirAltura(this.codigo)
    return render_template('alturaExclui.html', titulo="Excluir Altura", dados=this.msg)

#---------------altura---------------#

#---------------diabetes---------------#
    
@idoso.route('/diabetes.html', methods=['GET','POST'])
def diabetes():
    if request.method == 'POST':
        this.dia       = request.form['tNovaDiabetesData']
        this.hora      = request.form['tNovaDiabetesHora']
        this.diabetes = request.form['tNovaDiabetesDiabetes']
        this.msg = this.modelo.inserirDiabetes(this.dia, this.hora, this.diabetes)
    return render_template('diabetes.html', titulo="Diabetes", dados=this.msg)

@idoso.route('/diabetesConsulta.html', methods=['GET','POST'])
def consultaDiabetes():
    if request.method == 'GET':
        this.msg = this.modelo.consultarDiabetes()
    return render_template('diabetesConsulta.html', titulo="Consultar Diabetes", dados=this.msg)

@idoso.route('/diabetesAtualiza.html', methods=['GET','POST'])
def atualizaDiabetes():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarDiabetes(this.codigo, this.campo, this.dado)
    return render_template('diabetesAtualiza.html', titulo="Atualizar Diabetes", dados=this.msg)

@idoso.route('/diabetesExclui.html', methods=['GET','POST'])
def excluiDiabetes():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluir(this.codigo)
    return render_template('diabetesExclui.html', titulo="Excluir Diabetes", dados=this.msg)

#---------------diabetes---------------#

#---------------dieta---------------#
    
@idoso.route('/dieta.html', methods=['GET','POST'])
def dieta():
    if request.method == 'POST':
        this.dia       = request.form['tNovaDietaData']
        this.hora      = request.form['tNovaDietaHora']
        this.dieta = request.form['tNovaDietaDieta']
        this.msg = this.modelo.inserirDieta(this.dia, this.hora, this.dieta)
    return render_template('dieta.html', titulo="Dieta", dados=this.msg)

@idoso.route('/dietaConsulta.html', methods=['GET','POST'])
def consultaDieta():
    if request.method == 'GET':
        this.msg = this.modelo.consultarDieta()
    return render_template('dietaConsulta.html', titulo="Consultar Dieta", dados=this.msg)

@idoso.route('/dietaAtualiza.html', methods=['GET','POST'])
def atualizaDieta():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarDieta(this.codigo, this.campo, this.dado)
    return render_template('dietaAtualiza.html', titulo="Atualizar Dieta", dados=this.msg)

@idoso.route('/dietaExclui.html', methods=['GET','POST'])
def excluiDieta():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirDieta(this.codigo)
    return render_template('dietaExclui.html', titulo="Excluir Dieta", dados=this.msg)

#---------------dieta---------------#    
    
#---------------peso---------------#

@idoso.route('/peso.html', methods=['GET','POST'])
def peso():
    if request.method == 'POST':
        this.dia       = request.form['tNovaPesoData']
        this.hora      = request.form['tNovaPesoHora']
        this.peso = request.form['tNovaPesoPeso']
        this.msg = this.modelo.inserirPeso(this.dia, this.hora, this.peso)
    return render_template('peso.html', titulo="Peso", dados=this.msg)

@idoso.route('/pesoConsulta.html', methods=['GET','POST'])
def consultaPeso():
    if request.method == 'GET':
        this.msg = this.modelo.consultarPeso()
    return render_template('pesoConsulta.html', titulo="Consultar Peso", dados=this.msg)

@idoso.route('/pesoAtualiza.html', methods=['GET','POST'])
def atualizaPeso():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarPeso(this.codigo, this.campo, this.dado)
    return render_template('pesoAtualiza.html', titulo="Atualizar Peso", dados=this.msg)

@idoso.route('/pesoExclui.html', methods=['GET','POST'])
def excluiPeso():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirPeso(this.codigo)
    return render_template('pesoExclui.html', titulo="Excluir Peso", dados=this.msg)

#---------------peso---------------#

#---------------pressao---------------#

@idoso.route('/pressao.html', methods=['GET','POST'])
def pressao():
    if request.method == 'POST':
        this.dia       = request.form['tNovaPressaoData']
        this.hora      = request.form['tNovaPressaoHora']
        this.pressao = request.form['tNovaPressaoPressao']
        this.msg = this.modelo.inserirPressao(this.dia, this.hora, this.pressao)
    return render_template('pressao.html', titulo="Pressão", dados=this.msg)

@idoso.route('/pressaoConsulta.html', methods=['GET','POST'])
def consultaPressao():
    if request.method == 'GET':
        this.msg = this.modelo.consultarPressao()
    return render_template('pressaoConsulta.html', titulo="Consultar Pressão", dados=this.msg)

@idoso.route('/pressaoAtualiza.html', methods=['GET','POST'])
def atualizaPressao():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo  = request.form['tCampo']
        this.dado   = request.form['tDado']
        this.msg    = this.modelo.atualizarPressao(this.codigo, this.campo, this.dado)
    return render_template('pressaoAtualiza.html', titulo="Atualizar Pressão", dados=this.msg)

@idoso.route('/pressaoExclui.html', methods=['GET','POST'])
def excluiPressao():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluirPressao(this.codigo)
    return render_template('pressaoExclui.html', titulo="Excluir Pressão", dados=this.msg)

#---------------pressao---------------#

if __name__ == '__main__':
    idoso.run(debug=True, port=5000)