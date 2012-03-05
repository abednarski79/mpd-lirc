import sqlite3;
import sys;
import os;

title = sys.argv[1];
grade = sys.argv[2];
db_path = os.environ["MPD_LIRC_ROOT"] + "/commands/utils/votes.db"
connection = sqlite3.connect(db_path);
cursor = connection.cursor();
cursor.execute("insert into votes(title, grade) values (?, ?)", (title, grade));
connection.commit();
cursor.close();

