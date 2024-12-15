from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author, magazine):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author
        self.magazine_id = magazine
        self.create()

    def create(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        ''', (self.title, self.content, self.author_id, self.magazine_id))
        self.id = cursor.fetchall()
        conn.commit()
        conn.close()

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if 5 <= len(value) <= 50:
            self._title = value

    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM authors
            WHERE author_id = ?
        ''', (self.author.id,))
        author = cursor.fetchall()
        conn.close()
        return author
    
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM magazines
            WHERE author_id = ?
        ''', (self.magazine.id,))
        magazine = cursor.fetchall()
        conn.close()
        return magazine