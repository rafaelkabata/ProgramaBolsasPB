--EU UTILIZEI O POSTGREE, ONDE ELE CRIA O DATABASE DIRETO NO SOFTWARE E NAO POR QUERY.
--FAZER A CRIAÇÃO DE UM DATABASE ANTES DE RODAR AS QUERY.
--query para criação de database abaixo

--*create database concessionaria;
--*use concessionaria;

--CRIAÇÃO DA TABELA CLIENTE
CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(100),
    paisCliente VARCHAR(100)
);

--CRIAÇÃO DA TABELA COMBUSTIVEL
CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

--CRIAÇÃO DA TABELA CARRO
CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    idCombustivel INT,
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
	classiCarro varchar (50),
    anoCarro INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);



--CRIAÇÃO DA TABELA VENDEDOR
CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

--CRIAÇÃO DA TABELA LOCAÇÃO
CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

--INSERÇÃO DE DADOS NA TABELA CLIENTE
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
VALUES
(2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil'),
(3, 'Cliente três', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
(4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
(6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil'),
(10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil'),
(20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil'),
(22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil'),
(23, 'Cliente vinte e três', 'Eusébio', 'Ceará', 'Brasil'),
(5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil'),
(26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil');

--INSERÇÃO DE DADOS NA TABELA COMBUSTIVEL
INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
VALUES
(1, 'Gasolina'),
(2, 'Etanol'),
(3, 'Flex'),
(4, 'Diesel');

-- INSERÇÃO DE DADOS NA TABELA CARRO COM classiCarro
INSERT INTO Carro (idCarro, kmCarro, idCombustivel, marcaCarro, modeloCarro, classiCarro, anoCarro)
VALUES
(98, 25412, 1, 'Fiat', 'Fiat Uno', 'AKJHKN98JY76539', 2000),
(99, 20000, 1, 'Fiat', 'Fiat Palio', 'IKJHKN98JY76539', 2010),
(3, 121700, 1, 'VW', 'Fusca 78', 'IKJHKN98JY76539', 1978),
(10, 211800, 1, 'Fiat', 'Fiat 147', 'LKIUNS8JS76S39', 1996),
(7, 212800, 1, 'Fiat', 'Fiat 147', 'DKSHKNS8JS76S39', 1996),
(6, 21800, 1, 'Nissan', 'Versa', 'DKSHKNS8JS76S39', 2019),
(2, 10000, 2, 'Nissan', 'Versa', 'AKIUNS1JS76S39', 2019),
(4, 55000, 2, 'Nissan', 'Versa', 'AKIUNS1JS76S39', 2020),
(1, 1800, 3, 'Toyota', 'Corolla XEI', 'AAAKNS8JS76S39', 2023),
(5, 28000, 4, 'Nissan', 'Frontier', 'MSLUNS1JS76S39', 2022);


--INSERÇÃO DE DADOS NA TABELA VENDEDOR
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
VALUES
(5, 'Vendedor cinco', 0, 'São Paulo'),
(6, 'Vendedora seis', 1, 'São Paulo'),
(7, 'Vendedora sete', 1, 'Rio de Janeiro'),
(8, 'Vendedora oito', 1, 'Minas Gerais'),
(16, 'Vendedor dezesseis', 0, 'Amazonas'),
(30, 'Vendedor trinta', 0, 'Rio Grande do Sul'),
(31, 'Vendedor trinta e um', 0, 'Ceará'),
(32, 'Vendedora trinta e dois', 1, 'Mato Grosso do Sul');

--INSERÇÃO DE VALORES NA TABELA LOCAÇÃO
INSERT INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
VALUES
(1, 2, 98, 5, '2015-01-10', '10:00:00', 2, 100, '2015-01-12', '10:00:00'),
(2, 2, 98, 5, '2015-02-10', '12:00:00', 2, 100, '2015-02-12', '12:00:00'),
(3, 3, 99, 6, '2015-02-13', '12:00:00', 2, 150, '2015-02-15', '12:00:00'),
(4, 4, 99, 6, '2015-02-15', '13:00:00', 5, 150, '2015-02-20', '13:00:00'),
(5, 4, 99, 7, '2015-03-02', '14:00:00', 5, 150, '2015-03-07', '14:00:00'),
(6, 6, 3, 8, '2016-03-02', '14:00:00', 10, 250, '2016-03-12', '14:00:00'),
(7, 6, 3, 8, '2016-08-02', '14:00:00', 10, 250, '2016-08-12', '14:00:00'),
(8, 4, 3, 6, '2017-01-02', '18:00:00', 10, 250, '2017-01-12', '18:00:00'),
(9, 4, 3, 6, '2018-01-02', '18:00:00', 10, 280, '2018-01-12', '18:00:00'),
(10, 10, 10, 16, '2018-03-02', '18:00:00', 10, 50, '2018-03-12', '18:00:00'),
(11, 20, 7, 16, '2018-04-01', '11:00:00', 10, 50, '2018-04-11', '11:00:00'),
(12, 20, 6, 16, '2020-04-01', '11:00:00', 10, 150, '2020-04-11', '11:00:00'),
(13, 22, 2, 30, '2022-05-01', '08:00:00', 20, 150, '2022-05-21', '18:00:00'),
(14, 22, 2, 30, '2022-06-01', '08:00:00', 20, 150, '2022-06-21', '18:00:00'),
(15, 22, 2, 30, '2022-07-01', '08:00:00', 20, 150, '2022-07-21', '18:00:00'),
(16, 22, 2, 30, '2022-08-01', '08:00:00', 20, 150, '2022-07-21', '18:00:00'),
(17, 23, 4, 31, '2022-09-01', '08:00:00', 20, 150, '2022-09-21', '18:00:00'),
(18, 23, 4, 31, '2022-10-01', '08:00:00', 20, 150, '2022-10-21', '18:00:00'),
(19, 23, 4, 31, '2022-11-01', '08:00:00', 20, 150, '2022-11-21', '18:00:00'),
(20, 5, 1, 16, '2023-01-02', '18:00:00', 10, 880, '2023-01-12', '18:00:00'),
(21, 5, 1, 16, '2023-01-15', '18:00:00', 10, 880, '2023-01-25', '18:00:00'),
(22, 26, 5, 32, '2023-01-25', '08:00:00', 5, 600, '2023-01-30', '18:00:00'),
(23, 26, 5, 32, '2023-01-31', '08:00:00', 5, 600, '2023-02-05', '18:00:00'),
(24, 26, 5, 32, '2023-02-06', '08:00:00', 5, 600, '2023-02-11', '18:00:00'),
(25, 26, 5, 32, '2023-02-12', '08:00:00', 5, 600, '2023-02-17', '18:00:00'),
(26, 26, 5, 32, '2023-02-18', '08:00:00', 1, 600, '2023-02-19', '18:00:00');



-- ABAIXO SÃO AS QUERY DAS TABELAS DA MODELAGEM DIMENSIONAL

--VIEW PARA A DIMENSÃO CLIENTE
CREATE VIEW viewdimCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

--VIEW PARA A DIMENSÃO CARRO
CREATE VIEW viewdimCarro AS
SELECT c.idCarro, c.kmCarro, c.classiCarro, c.marcaCarro, c.modeloCarro, c.anoCarro, comb.tipoCombustivel
FROM Carro c
INNER JOIN Combustivel comb ON c.idCombustivel = comb.idCombustivel;




--VIEW PARA A DIMENSÃO VENDEDOR
CREATE VIEW viewdimVendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;

--VIEW PARA A DIMENSÃO COMBUSTIVEL
CREATE VIEW viewdimCombustivel AS
SELECT idCombustivel, tipoCombustivel
FROM Combustivel;

--VIEW PARA A DIMENSÃO DE FATOS
CREATE VIEW viewfatoLocacao AS
SELECT
    L.idLocacao,
    L.idCliente,
    L.idCarro,
    C.idCombustivel,
    L.idVendedor,
    L.dataLocacao,
    L.horaLocacao,
    L.qtdDiaria,
    L.vlrDiaria,
    L.dataEntrega,
    L.horaEntrega
FROM Locacao L
JOIN Carro C ON L.idCarro = C.idCarro;




