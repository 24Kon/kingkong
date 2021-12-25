create table store (id serial, product_name varchar(32), category varchar(32),
            producer varchar(32), data date, price numeric check(price>0.0), 
            provider varchar(32), data_end date);


insert into store (product_name, category, producer, data, price, provider, data_end) 
    values ('orange', 'fruit', 'premium group', '2021-10-21', '30.00', 'quantula', '2021-11-04'), 
    ('potato', 'vegetable', 'premium group', '2021-10-06', '15.00', 'quantula', '2022-04-06'), 
    ('bread', 'bakery', 'novo-barakyi', '2021-10-21', '21.00', 'desna', '2021-10-09'), 
    ('ketchup', 'sauce', 'heinz', '2021-10-14', '100.00', 'warateka', '2021-11-14');


select category, count (*) from store group by category;
select data, count (*) from store group by data;
select producer, count(*) from store group by producer;
