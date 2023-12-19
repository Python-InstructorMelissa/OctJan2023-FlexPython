from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash



class Owner:
    db = 'ownerValReg'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM owner;'
        results = connectToMySQL(cls.db).query_db(query)
        owners = []
        for row in results:
            owners.append(cls(row))
        return owners

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM owner WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getEmail(cls, data):
        query = 'SELECT * FROM owner WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO owner (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE owner SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM owner WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
    

    @staticmethod
    def validation(owner):
        is_valid = True
        if len(owner['first_name']) < 4:
            is_valid = False
            flash("We need to know how to address you.")
        return is_valid