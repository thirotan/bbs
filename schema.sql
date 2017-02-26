drop table if exists threads;
create table threads(
  id integer primary key autoincrement,
  thread_name text
)engine=InnoDB  DEFAULT CHARSET=utf8;

drop table if exists titles;
create table titles(
  id integer primary key autoincrement,
  thread_id integer,
  title text,
  created_at datetime,
  foreign key(thread_id) references threads(id)
) engine=InnoDB  DEFAULT CHARSET=utf8;

drop table if exists messages;
create table messages(
  board_id integer,
  name text,
  message text,
  ip_addr text,
  created_at datetime,
  foreign key(board_id) references board_titles(id)
) engine=InnoDB DEFAULT CHARSET=utf8;  
