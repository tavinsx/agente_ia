import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
import os

class DBmeneger: # Manager
    # sqlite3 nome_db.db
    # .schema
    # .tables
    def __init__(self, db_path='base_conhecimento.db'):
        if not os.path.exists(db_path):
            self._create_db_file(db_path)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._create_table()
    
    def _create_db_file(self, db_path):
        open(db_path, 'a').close()


    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                embedding BLOB NOT NULL
            )
        ''')
        self.conn.commit()

    def add_content(self, text):

        embedding = self.model.encode([text])[0]

        emb_bytes = embedding.tobytes()
        
        self.cursor.execute("INSERT INTO knowledge_base(content, embedding) VALUES (?, ?)", (text, emb_bytes))

        self.conn.commit()

    def search(self, query, top_k=3):

        query_embedding = self.model.encode([query])[0]
        
        self.cursor.execute("SELECT id, content, embedding FROM knowledge_base")
        
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            emb = np.frombuffer(row[2], dtype=np.float32)

            sim = np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb))

            results.append((row[0], row[1], sim))

            results.sort(key=lambda x: x[2], reverse =True)
            return results[:top_k]

if __name__ == "__main__":
    db = DBmeneger(db_path='base_conhecimento.db')