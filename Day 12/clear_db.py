import sqlite3

conn = sqlite3.connect("crop.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM crops")

conn.commit()

conn.close()

print("All records deleted successfully")