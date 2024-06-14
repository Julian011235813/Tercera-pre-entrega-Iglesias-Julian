#import sqlite3


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


cursor.execute("ALTER TABLE appdeinicio_auto RENAME TO appdeinicio_auto_old;")


cursor.execute("""
CREATE TABLE appdeinicio_auto (
    id INTEGER PRIMARY KEY,
    marca TEXT,
    modelo TEXT
);
""")

cursor.execute("""
INSERT INTO appdeinicio_auto (id, marca, modelo)
SELECT id, marca, modelo
FROM appdeinicio_auto_old;
""")


cursor.execute("DROP TABLE appdeinicio_auto_old;")


conn.commit()
conn.close()



