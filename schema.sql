drop table if exists threads;
create table threads(
  id integer primary key autoincrement,
  thread_name text
)engine=InnoDB  DEFAULT CHARSET=utf8;

drop table if exists board_titles;
create table board_titles(
  id integer primary key autoincrement,
  thread_id integer,
  thread_name text,
  created_at datetime,
  foreign key(thread_id) references threads(id)
) engine=InnoDB  DEFAULT CHARSET=utf8;

drop table if exists board_messages;
create table board_messages(
  board_id integer,
  name text,
  message text,
  ip_addr text,
  created_at datetime,
  foreign key(board_id) references board_titles(id)
) engine=InnoDB DEFAULT CHARSET=utf8;  
