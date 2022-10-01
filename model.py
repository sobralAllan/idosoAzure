import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
     
    #----------INSERIR----------#

    def inserirIdoso(self, nome, apelido, nsus, rg, cpf, mae, dataDeNascimento, sexo, municipioN, nacionalidade, paisN, alfa, escolaridade, raca, religiao, ocupacao, conjugal, ubs, alergia, deficiencia, qualD, sangue, fator, rua, num, complemento, bairro, ref, cep, municipioE, estado, telefone, celular, email, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10, pergunta11, pergunta12, refNome, refNascimento, refVinculo, refEndereco, refTel, refMora, refDataInfo):
        try:
            sql = "Insert into dados(codigo, nome, apelido, NSUS, RG, CPF, mae, dataDeNascimento, sexo, municipioN, nacionalidade, paisN, alfa, escolaridade, raca, religiao, ocupacao, conjugal, UBS, alergia, deficiencia, qualD, sangue, fator, rua, num, complemento, bairro, ref, CEP, municipioE, estado, telefone, celular, email, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10, pergunta11, pergunta12, refNome, refNascimento, refVinculo, refEndereco, refTel, refMora, refDataInfo) values('','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nome, apelido, nsus, rg, cpf, mae, dataDeNascimento, sexo, municipioN, nacionalidade, paisN, alfa, escolaridade, raca, religiao, ocupacao, conjugal, ubs, alergia, deficiencia, qualD, sangue, fator, rua, num, complemento, bairro, ref, cep, municipioE, estado, telefone, celular, email, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10, pergunta11, pergunta12, refNome, refNascimento, refVinculo, refEndereco, refTel, refMora, refDataInfo)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} cadastro realizado!".format(self.con.rowcount)
        except Exception as erro:
            return erro
    
    def inserirAgenda(self, dia, hora, descricao):
        try:
            sql = "Insert into agenda(codigo, dia, hora, descricao) values('','{}','{}','{}')".format(dia, hora, descricao)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} evento cadastrado!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def inserirAjuda(self, duvida, ajuda):
        try:
            sql = "Insert into ajuda(codigo, duvida, ajuda) values('','{}','{}')".format(duvida, ajuda)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} dúvida/ajuda cadastrada!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def inserirAltura(self, dia, hora, altura):
        try:
            sql = "Insert into altura(codigo, dia, hora, altura) values('','{}','{}','{}')".format(dia, hora, altura)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} dado de altura cadastrado!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def inserirDiabetes(self, dia, hora, diabetes):
        try:
            sql = "Insert into diabetes(codigo, dia, hora, diabetes) values('','{}','{}','{}')".format(dia, hora, diabetes)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} dado de diabetes cadastrado!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def inserirDieta(self, dia, hora, dieta):
        try:
            sql = "Insert into dieta(codigo, dia, hora, dieta) values('','{}','{}','{}')".format(dia, hora, dieta)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} dado de dieta cadastrado!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def inserirPeso(self, dia, hora, peso):
        try:
            sql = "Insert into peso(codigo, dia, hora, peso) values('','{}','{}','{}')".format(dia, hora, peso)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} dado de peso cadastrado!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def inserirPressao(self, dia, hora, pressao):
        try:
            sql = "Insert into pressao(codigo, dia, hora, pressao) values('','{}','{}','{}')".format(dia, hora, pressao)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} dado de pressao cadastrado!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    #----------CONSULTAR----------#       

    def consultarIdoso(self):
        try:
            sql = "select * from dados"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, nome, apelido, nsus, rg, cpf, mae, dataDeNascimento, sexo, municipioN, nacionalidade, paisN, alfa, escolaridade, raca, religiao, ocupacao, conjugal, ubs, alergia, deficiencia, qualD, sangue, fator, rua, num, complemento, bairro, ref, cep, municipioE, estado, telefone, celular, email, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10, pergunta11, pergunta12, refNome, refNascimento, refVinculo, refEndereco, refTel, refMora, refDataInfo) in self.con:
                msg = msg + "\nCódigo: {}\n\n  Informações do idoso \n\n•Nome Completo: {}\n•Apelido/Nome Social: {}\n•Número Cartão Nacional de Saúde: {}\n•Documento de Identidade/RG: {}\n•CPF: {}\n•Nome Completo da Mãe: {}\n•Data de Nascimento: {}\n•Sexo: {}\n•Município de Nascimento: {}\n•Nacionalidade: {}\n•País de Nascimento: {}\n•Sabe ler e escrever?: {}\n•Escolaridade: {}\n•Raça/Cor: {}\n•Tem religião?: {}\n•Ocupação/Profissional Principal: {}\n•Situação conjugal: {}\n•Unidade Básica de Saúde que frequenta: {}\n•Tem alguma alergia de maior gravidade? Especificar: {}\n•Tem alguma deficiência?: {}\n•Qual?: {}\n•Grupo Sanguíneo: {}\n•Fator RH: {}\n\n  Endereço residencial \n\n•Rua/Avenida/Praça: {}\n•Número: {}\n•Complemento: {}\n•Bairro: {}\n•Ponto de Referência: {}\n•CEP: {}\n•Município: {}\n•Estado: {}\n•Telefone: {}\n•Celular: {}\n•Email: {}\n\n  Informações sociofamiliares \n\n•Você mora sozinho(a)?: {}\n•Você mora com familiares?: {}\n•Você mora com seu(sua) cônjuge ou companheiro(a)?: {}\n•Você reside em Instituição de Longa Permanência para Idosos (ILPI), abrigo ou casa de repouso?: {}\n•Nos últimos 30 dias, você se encontrou com amigos ou familiares para como ir ao cinema ou à igreja, passear ou caminhar junto?: {}\n•Em caso de necessidade, você conta com alguém para acompanhá-lo(a) à unidade de saúde ou a uma consulta?: {}\n•Você tem fácil acesso aos serviços de farmácia, padaria ou supermercado?: {}\n•Você tem fácil acesso a transporte?: {}\n•Você trabalha atualmente?: {}\n•Você recebe aposentadoria ou pensão?: {}\n•Você recebe Benefício de Prestação Continuada (BPC)?: {}\n•Você recebe Bolsa Família?: {}\n\n  Pessoas de Referência \n\nDados de pessoas que possam ser contatadas em caso de urgência. \n•Nome Completo: {}\n•Data de Nascimento: {}\n•Vínculo: {}\n•Endereço: {}\n•Telefone/Celular: {}\n•Esta pessoa mora com você?: {}\n•Data dessa informação: {}\n\n".format(codigo, nome, apelido, nsus, rg, cpf, mae, dataDeNascimento, sexo, municipioN, nacionalidade, paisN, alfa, escolaridade, raca, religiao, ocupacao, conjugal, ubs, alergia, deficiencia, qualD, sangue, fator, rua, num, complemento, bairro, ref, cep, municipioE, estado, telefone, celular, email, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10, pergunta11, pergunta12, refNome, refNascimento, refVinculo, refEndereco, refTel, refMora, refDataInfo)
            return msg
        except Exception as erro:
            return erro

    def consultarAgenda(self):
        try:
            sql = "select * from agenda"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, dia, hora, descricao) in self.con:
                msg = msg + "\nCódigo: {}\nData: {}\nHorário: {}\nDescrição: {}".format(codigo, dia, hora, descricao)
            return msg
        except Exception as erro:
            return erro
        
    def consultarAjuda(self):
        try:
            sql = "select * from ajuda"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, duvida, ajuda) in self.con:
                msg = msg + "\nCódigo: {}\n•Dúvida: {}\n•Resposta: {}".format(codigo, duvida, ajuda)
            return msg
        except Exception as erro:
            return erro

    def consultarAltura(self):
        try:
            sql = "select * from altura"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, dia, hora, altura) in self.con:
                msg = msg + "\nCódigo: {}\n•Data: {}\n•Horário: {}\n•Altura: {}".format(codigo, dia, hora, altura)
            return msg
        except Exception as erro:
            return erro

    def consultarDiabetes(self):
        try:
            sql = "select * from diabetes"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, dia, hora, diabetes) in self.con:
                msg = msg + "\nCódigo: {}\n•Data: {}\n•Horário: {}\n•Diabetes: {}".format(codigo, dia, hora, diabetes)
            return msg
        except Exception as erro:
            return erro

    def consultarDieta(self):
        try:
            sql = "select * from dieta"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, dia, hora, dieta) in self.con:
                msg = msg + "\nCódigo: {}\n•Data: {}\n•Horário: {}\n•Dieta: {}".format(codigo, dia, hora, dieta)
            return msg
        except Exception as erro:
            return erro

    def consultarPeso(self):
        try:
            sql = "select * from peso"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, dia, hora, peso) in self.con:
                msg = msg + "\nCódigo: {}\n•Data: {}\n•Horário: {}\n•Peso: {}".format(codigo, dia, hora, peso)
            return msg
        except Exception as erro:
            return erro

    def consultarPressao(self):
        try:
            sql = "select * from pressao"
            self.con.execute(sql)
            msg = ""
            
            for(codigo, dia, hora, pressao) in self.con:
                msg = msg + "\nCódigo: {}\n\n•Data: {}\n•Horário: {}\n•Pressão: {}\n\n".format(codigo, dia, hora, pressao)
            return msg
        except Exception as erro:
            return erro

    #----------ATUALIZAR----------#

    def atualizarIdoso(self, cod, campo, novoDado):
        try:
            sql = "update dados set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarAgenda(self, cod, campo, novoDado):
        try:
            sql = "update agenda set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarAjuda(self, cod, campo, novoDado):
        try:
            sql = "update ajuda set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarAltura(self, cod, campo, novoDado):
        try:
            sql = "update altura set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarDiabetes(self, cod, campo, novoDado):
        try:
            sql = "update diabetes set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarDieta(self, cod, campo, novoDado):
        try:
            sql = "update dieta set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarPeso(self, cod, campo, novoDado):
        try:
            sql = "update peso set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def atualizarPressao(self, cod, campo, novoDado):
        try:
            sql = "update pressao set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    #----------EXCLUIR----------#

    def excluirIdoso(self, cod):
        try:
            sql = "delete from dados where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirAgenda(self, cod):
        try:
            sql = "delete from agenda where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirAjuda(self, cod):
        try:
            sql = "delete from ajuda where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirAltura(self, cod):
        try:
            sql = "delete from altura where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirDiabetes(self, cod):
        try:
            sql = "delete from diabetes where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirDieta(self, cod):
        try:
            sql = "delete from dieta where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirPeso(self, cod):
        try:
            sql = "delete from peso where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def excluirPressao(self, cod):
        try:
            sql = "delete from pressao where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount) 
        except Exception as erro:
            return erro
        
    def tratarData(self, texto):
        separado = texto.split("/")
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)