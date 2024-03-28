create schema if not exists Viagens;
use viagens;

create table if not exists usuarios (
	id int,
    nome varchar(225) not null comment'nome do usuário',
    email varchar(100) not null unique comment'e-mail do usuário',
    endereco varchar(50) not null comment'endereco do usuário',
    data_nascimento date not null comment'data de nascimento do usuário'
    );
    
CREATE TABLE if not exists destinos (
  id INT,
  nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
  descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE if not exists reservas (
  id INT COMMENT 'Identificador único da reserva',
  id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
  id_destino INT COMMENT 'Referência ao ID do destino da reserva',
  data_v DATE COMMENT 'Data da reserva',
  status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc.)'
);

#inserts

insert into usuarios (id, nome, email, endereco, data_nascimento) values
(1, 'Beatriz cavalcante', 'beatriz@email.com', 'rua dos patos', '2001-11-13'),
(2, 'Maria Santos', 'maria@example.com', 'Rua B, 456, Cidade Y, Estado Z','1985-08-22'),
(3, 'Pedro Souza', 'pedro@example.com', 'Avenida C, 789, Cidade X, Estado Y', '1998-02-10');

insert into destinos (id, nome, descricao) values
(1,'Praia de Boa Viagem','Não vi tutubas'),
(2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

insert into reservas (id, id_usuario, id_destino, data_v, status) values
(1, 1, 1, '2023-07-10', 'confirmada'),
(2, 2, 2, '2023-08-05', 'pendente'),
(3, 3, 3, '2023-09-20', 'cancelada');



#leitura

select * from usuarios;
select * from usuarios
	where id = 1 or nome like '%Maria%';
select * from destinos;
select * from reservas;

#Atualizações

UPDATE usuarios SET endereco = 'Nova Rua, 123' WHERE email = 'joao@example.com';

update usuarios set endereco = 'Rua B, 456, Cidade Y, Estado Z' where id = 1;

delete from destinos where nome = 'Cachoeira do Vale Verde';

#Alteração 

create table if not exists usuarios_Nova (
	id int,
    nome varchar(225) not null comment'nome do usuário',
    email varchar(100) not null unique comment'e-mail do usuário',
    endereco varchar(100) not null comment'endereco do usuário',
    data_nascimento date not null comment'data de nascimento do usuário'
    );
    
insert into usuarios_Nova (id, nome, email, endereco, data_nascimento) 
select id, nome, email, endereco, data_nascimento
from usuarios;

select * from usuarios_Nova;

#59 a 71 foi criado uma nova tabela e se aproveitou os dados de uma outra tabela
drop table usuarios;
alter table usuarios_Nova rename usuarios;

alter table usuarios modify column endereco varchar(150);

#Chaves primária e estrangeira


#chave primaria
alter table usuarios
modify column id int auto_increment,
add primary key (id);

alter table destinos
modify column id int auto_increment,
add primary key (id);

alter table reservas
modify column id int auto_increment,
add primary key (id);

#chave estrangeira
alter table reservas
add constraint fk_reservas_usuarios #recebe_Origem
foreign key(id_usuario) references usuarios(id);

alter table reservas
add constraint fk_reservas_destinos #recebe_Origem
foreign key(id_destino) references destinos(id);


alter table reservas
add constraint fk_usuarios
foreign key (id_usuario) references usuarios(id)
on delete cascade; 

#Normalização de dados
alter table usuarios
add rua varchar(100) comment'só em colocar add já fica entendido que é sobre colunas',
add numero varchar(10),
add cidade varchar(50),
add estado varchar(20);

-- Copia os dados da tabela original para a nova tabela
UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);

alter table usuarios
drop column endereco;

#Junções - join

select * from usuarios
inner join reservas
on usuarios.id = reservas.id_usuario
inner join destinos on reservas.id_destino = destinos.id;

INSERT INTO viagens.destinos ( nome, descricao) VALUES 
('Deestino sem reserva', 'Uma bela praia com areias brancas e mar cristalino');

select * from reservas rs
right join destinos ds
on rs.id_destino = ds.id;

#sub consultas

select * from destinos
where id not in (select id_destino from reservas);

#funções agregadoras

#select count(*) as total_usuarios from usuarios; (dessa forma para nomear a coluna)
select count(*) from usuarios
inner join reservas on usuarios.id = reservas.id_usuario;

select max(timestampdiff(year, data_nascimento, current_date())) as maior_idade
from usuarios;

#Ordenação

select count(*) from reservas
group by id_destino;

SELECT nome
FROM usuarios
ORDER BY nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome DESC;


#indide de busca

-- Inserindo massa de dados --

INSERT INTO usuarios (nome, email, data_nascimento, rua) VALUES
('João Silva', 'joao.silva@example.com', '1990-01-01', 'Rua A'),
('Maria Santos', 'maria.santos@example.com', '1992-03-15', 'Rua B'),
('Pedro Almeida', 'pedro.almeida@example.com', '1985-07-10', 'Rua C'),
('Ana Oliveira', 'ana.oliveira@example.com', '1998-12-25', 'Rua D'),
('Carlos Pereira', 'carlos.pereira@example.com', '1991-06-05', 'Rua E'),
('Laura Mendes', 'laura.mendes@example.com', '1994-09-12', 'Rua F'),
('Fernando Santos', 'fernando.santos@example.com', '1988-02-20', 'Rua G'),
('Mariana Costa', 'mariana.costa@example.com', '1997-11-30', 'Rua H'),
('Ricardo Rodrigues', 'ricardo.rodrigues@example.com', '1993-04-18', 'Rua I'),
('Camila Alves', 'camila.alves@example.com', '1989-08-08', 'Rua J'),
('Bruno Carvalho', 'bruno.carvalho@example.com', '1995-03-25', 'Rua K'),
('Amanda Silva', 'amanda.silva@example.com', '1996-12-02', 'Rua L'),
('Paulo Mendonça', 'paulo.mendonca@example.com', '1999-07-20', 'Rua M'),
('Larissa Oliveira', 'larissa.oliveira@example.com', '1987-10-15', 'Rua N'),
('Fernanda Sousa', 'fernanda.sousa@example.com', '1992-05-08', 'Rua O'),
('Gustavo Santos', 'gustavo.santos@example.com', '1993-09-18', 'Rua P'),
('Helena Costa', 'helena.costa@example.com', '1998-02-22', 'Rua Q'),
('Diego Almeida', 'diego.almeida@example.com', '1991-11-27', 'Rua R'),
('Juliana Lima', 'juliana.lima@example.com', '1997-04-05', 'Rua S'),
('Rafaela Silva', 'rafaela.silva@example.com', '1996-01-10', 'Rua T'),
('Lucas Pereira', 'lucas.pereira@example.com', '1986-08-30', 'Rua U'),
('Fábio Rodrigues', 'fabio.rodrigues@example.com', '1989-03-12', 'Rua V'),
('Isabela Santos', 'isabela.santos@example.com', '1994-12-07', 'Rua W'),
('André Alves', 'andre.alves@example.com', '1995-09-28', 'Rua X'),
('Clara Carvalho', 'clara.carvalho@example.com', '1990-02-15', 'Rua Y'),
('Roberto Mendes', 'roberto.mendes@example.com', '1992-07-21', 'Rua Z'),
('Mariana Oliveira', 'mariana.oliveira@example.com', '1997-05-03', 'Av. A'),
('Gustavo Costa', 'gustavo.costa@example.com', '1998-11-16', 'Av. B'),
('Lara Sousa', 'lara.sousa@example.com', '1993-06-09', 'Av. C'),
('Pedro Lima', 'pedro.lima@example.com', '1996-09-27', 'Av. D');




EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";

EXPLAIN SELECT * FROM usuarios us
INNER JOIN reservas rs
ON us.id = rs.id_usuario
WHERE nome = "Maria";


CREATE INDEX idx_nome ON usuarios (nome);

EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";