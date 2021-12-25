create table work(id serial primary key, title varchar(32), description varchar(32));
insert into work (title, description) values 
            ('dell', 'tester'), ('ibm', 'system_admin'), 
            ('oracle', 'tester'), ('dell', 'manager');
select * from work;


create table phone( id serial primary key, first_name varchar(32), 
            last_name varchar(32), phone_number integer,  
            mail varchar(32), work_id integer references work(id));
insert into phone (first_name, last_name, phone_number, mail, work_id) values 
    ('ahmed', 'aziza', '12345', 'ahmed1@mail', 1), ('ali', 'talib', '56789', 'ali23@mail', 2),
    ('alex', 'bobov', '54321', 'alex2@mail', 4), ('volodya', 'petruha', '98765', 'volod1@mail', 3);
select * from phone;