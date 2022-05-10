import sqlite3

class Countletters:
    def __init__(self, id, word, img, letters, syllables ):
        self.id = id
        self.word = word
        self.img = img
        self.letters = letters
        self.syllables = syllables

    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'img': self.img,
            'letters': self.letters,
            'syllables': self.syllables
        }

class CountlettersRepository:
    def __init__ (self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists countLetters(
                "id" varchar PRIMARY KEY, 
                "word" varchar,
                "img" varchar,
                "letters" varchar,
                "syllables" varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_texts(self):
        sql = """select * from countletter"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        result = []
        for item in data:
            countletter = Countletters(**item)
            result.append(countletter)

        return result