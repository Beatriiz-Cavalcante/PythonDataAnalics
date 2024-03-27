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












