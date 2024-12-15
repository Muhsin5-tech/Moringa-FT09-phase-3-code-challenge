from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author = author_id
        self.magazine = magazine_id
        self.create()

    def create(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        ''', (self.title, self.content, self.author.id, self.magazine.id))
        self.id = cursor.lastrowid()
        conn.commit()
        conn.close()

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be between 5 and 50 characters.")

    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM authors
            WHERE author_id = ?
        ''', (self.author_id,))
        author = cursor.fetchall()
        conn.close()
        return author
    
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM magazines
            WHERE author_id = ?
        ''', (self.magazine_id,))
        magazine = cursor.fetchall()
        conn.close()
        return magazine