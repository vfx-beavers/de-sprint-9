create schema if not exists cdm;

drop table if exists cdm.user_product_counters;

create table if not exists cdm.user_product_counters (
	id serial not null,
	user_id uuid not null,
	product_id uuid not null,
	product_name character varying not null,
	order_cnt int not null,
	constraint user_product_counters_id_pk primary key(id),
	constraint order_cnt_check check (order_cnt >= 0),
	constraint user_id_product_id_un_idx unique (user_id, product_id)
);

drop table if exists cdm.user_category_counters;

create table if not exists cdm.user_category_counters (
	id serial not null,
	user_id uuid not null,
	category_id uuid not null,
	category_name character varying not null,
	order_cnt int not null,
	constraint user_category_counters_id_pk primary key(id),
	constraint order_cnt_check check (order_cnt >= 0),
	constraint user_id_category_id_un_idx unique (user_id, category_id)
);
