create table phone (id serial primary key, 
                first_name varchar(32), 
                last_name varchar(32), 
                phone_number integer, 
                mail varchar(32), 
                company varchar (32), job_title varchar(32));
insert into phone (first_name, last_name, phone_number, mail, company, job_title) values 
            ('ahmed', 'aziza', '12345', 'ahmed12@mail', 'dell', 'tester'), 
            ('ali', 'talib', '56789', 'ali23@mail', 'ibm', 'system_admin'), 
            ('volodya', 'petruha', '54321', 'volod@mail', 'oracle', 'tester'), 
            ('daniil', 'sidorov', '98765', 'danchik@mail', 'ibm', 'system_admin'), 
            ('alex', 'bobov', '76543', 'alex@mail', 'dell', 'manager');
            select company, count(*) from phone group by company;
            select job_title, count(*) from phone group by job_title;
            
