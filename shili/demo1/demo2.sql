drop table if exists contents;
create table contents (
    id integer primary key autoincrement,
	title string not null,
	text string not null
);
