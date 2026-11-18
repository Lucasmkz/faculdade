# faculade
create database LojaInformatica;

use LojaInformatica;

create table categorias (
  id_categoria int,
  nome_categoria varchar(50),
  primary key(id_categoria)
);

create table produtos (
  id_produto int,
  nome_produto varchar(100),
  quantidade int,
  preco decimal(10,2),
  id_categoria int,
  primary key(id_produto),
  foreign key (id_categoria) references categorias(id_categoria)
);

insert into categorias
(id_categoria, nome_categoria)
values
(1, 'Computadores'),
(2, 'Periféricos'),
(3, 'Armazenamento'),
(4, 'Acessórios'),
(5, 'Impressão');

insert into produtos
(id_produto, nome_produto, quantidade, preco, id_categoria)
values
(1, 'Notebook', 50, 3500, 1),
(2, 'Mouse sem fio', 200, 85.9, 2),
(3, 'SSD 480GB', 80, 299.9, 3),
(4, 'Teclado mecânico', 120, 250, 2),
(5, 'Cabo HDMI', 300, 35.5, 4),
(6, 'Impressora laser', 25, 1200, 5),
(7, 'Computador desktop', 40, 2800, 1);

select * from produtos;

select nome_produto, nome_categoria
from produtos, categorias
where produtos.id_categoria = categorias.id_categoria;

select nome_categoria, sum(quantidade)
from categorias, produtos
where produtos.id_categoria = categorias.id_categoria
group by nome_categoria;

select nome_produto, preco
from produtos
where preco > 200;

select nome_produto, preco
from produtos
order by preco desc;

select sum(preco * quantidade) as total_estoque_loja
from produtos;

update produtos
set nome_produto = 'Mouse sem fio ergonômico'
where id_produto = 2;

select * from produtos;

delete from produtos
where id_categoria = 4;

select * from produtos;

delete from categorias
where id_categoria = 4;

select * from categorias;

drop table produtos;

drop table categorias;

drop database LojaInformatica;
