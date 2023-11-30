from flask_app.config.mysqlconnection import connectToMySQL



class Image:
    db = 'userImages'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.url = data['url']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM image;'
        results = connectToMySQL(cls.db).query_db(query)
        images = []
        for row in results:
            images.append(cls(row))
        return images

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM image WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO image (title, url, user_id) VALUES (%(title)s, %(url)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass