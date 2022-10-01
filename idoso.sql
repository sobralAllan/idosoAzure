create database idoso;
use idoso;

create table dados(
codigo int primary key not null auto_increment,
nome varchar(20),
apelido varchar(20),
NSUS  varchar(15),
RG varchar(9),
CPF varchar(11),
mae varchar(40),
dataDeNascimento date,
sexo varchar(10),
municipioN varchar(30),
nacionalidade varchar(15),
paisN varchar(20),
alfa varchar(3),
escolaridade varchar(15),
raca varchar(15),
religiao varchar(30),
ocupacao varchar(30),
conjugal varchar(30),
UBS varchar(30),
alergia varchar(20),
deficiencia varchar(3),
qualD varchar(15),
sangue varchar(2),
fator varchar(1),
rua varchar(20),
num varchar(10),
complemento varchar(10),
bairro varchar(15),
ref varchar(20),
CEP varchar(9),
municipioE varchar(30),
estado varchar(20),
telefone varchar(15),
celular varchar(15),
email varchar(30),
pergunta1 varchar(3),
pergunta2 varchar(3),
pergunta3 varchar(3),
pergunta4 varchar(3),
pergunta5 varchar(3),
pergunta6 varchar(3),
pergunta7 varchar(3),
pergunta8 varchar(3),
pergunta9 varchar(3),
pergunta10 varchar(3),
pergunta11 varchar(3),
pergunta12 varchar(3),
refNome varchar(20),
refNascimento date,
refVinculo varchar(15),
refEndereco varchar(50),
refTel varchar(15),
refMora varchar(3),
refDataInfo date
)engine = InnoDB;


create table agenda(
codigo int primary key not null auto_increment,
dia date,
hora time,
descricao varchar(30) 
)engine = InnoDB;

create table ajuda(
codigo int primary key not null auto_increment,
duvida varchar(100),
ajuda varchar(100)
)engine = InnoDB;

create table altura(
codigo int primary key not null auto_increment,
dia date,
hora time,
altura varchar(10)
)engine = InnoDB;

create table diabetes(
codigo int primary key not null auto_increment,
dia date,
hora time,
diabetes varchar(10)
)engine = InnoDB;

create table dieta(
codigo int primary key not null auto_increment,
dia date,
hora time,
dieta varchar(100)
)engine = InnoDB;

create table peso(
codigo int primary key not null auto_increment,
dia date,
hora time,
peso varchar(10)
)engine = InnoDB;

create table pressao(
codigo int primary key not null auto_increment,
dia date,
hora time,
pressao varchar(10)
)engine = InnoDB;







select * from dados;