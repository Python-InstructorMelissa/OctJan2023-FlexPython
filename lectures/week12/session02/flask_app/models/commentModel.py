from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash



class Comment:
    db = 'commentValReg'
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']
        self.receiver_id = data['receiver_id']
        self.owner_id = data['owner_id']
        self.to_id = data['to_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM comment;'
        results = connectToMySQL(cls.db).query_db(query)
        comments = []
        for row in results:
            comments.append(cls(row))
        return comments

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM comment WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # @classmethod
    # def getEmail(cls, data):
    #     query = 'SELECT * FROM comment WHERE email = %(email)s;'
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     if len(results) < 1:
    #         return False
    #     return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO comment (comment, user_id, receiver_id) VALUES (%(comment)s, %(user_id)s, %(receiver_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    # @classmethod
    # def update(cls, data):
    #     query = 'UPDATE comment SET comment = %(comment)s, last_name = %(last_name)s WHERE id = %(id)s;'
    #     return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM comment WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    

    @staticmethod
    def validation(comment):
        is_valid = True
        if len(comment['comment']) < 4:
            is_valid = False
            flash("We need to know how to address you.")
        return is_valid