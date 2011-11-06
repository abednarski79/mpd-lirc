import sqlite3;
import sys;

title = sys.argv[1];
grade = sys.argv[2];

connection = sqlite3.connect('/root/scripts/mpd/votes.db');
cursor = connection.cursor();
cursor.execute("insert into votes(title, grade) values (?, ?)", (title, grade));
connection.commit();
cursor.close();

