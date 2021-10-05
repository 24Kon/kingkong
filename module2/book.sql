create table book (
	 	id serial primary key, name varchar(32),
		author varchar(32), year date, 
		category varchar(32), pages int);
		
		insert into book (name, author, year, category, pages) values 
		('world and war', 'tolstoy', '1996-01-18', 'roman', '1300'),
		('crime and punish', 'dostoevski', '2000-01-18', 'roman', '672'),
		('hell', 'dante', '1990-01-12', 'poema', '512'),
		('player', 'dostoevski', '2001-09-12', 'roman', '416'),
		('paradise', 'dante', '2000-01-18', 'poema', '785'),
		('childhood', 'tolstoy', '1990-01-12', 'roman', '211');

		select category, count (*) from book group by category;
		select year, count (*) from book group by year;

		select author, count(*) from book where author = 'tolstoy' group by author;
		select author, count(*) from book where author = 'dante' group by author;
		select author, count(*) from book where author = 'dostoevski' group by author;
