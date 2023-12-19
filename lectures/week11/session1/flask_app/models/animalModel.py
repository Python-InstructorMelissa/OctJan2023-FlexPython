from flask_app.config.mysqlconnection import connectToMySQL


class Animal:
    db = 'mayhem'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.species = data['species']
        self.appendage = data['appendage']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM animal;'
        results = connectToMySQL(cls.db).query_db(query)
        animals = []
        for row in results:
            animals.append(cls(row))
        return animals

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM animal WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO animal (name, species, appendage, user_id) VALUES (%(name)s, %(species)s, %(appendage)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE animal SET name = %(name)s  WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM animal WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
