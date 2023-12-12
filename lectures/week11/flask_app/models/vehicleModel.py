from flask_app.config.mysqlconnection import connectToMySQL


class Vehicle:
    db = 'mayhem'
    def __init__(self, data):
        self.id = data['id']
        self.style = data['style']
        self.color = data['color']
        self.name = data['name']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM vehicle;'
        results = connectToMySQL(cls.db).query_db(query)
        vehicles = []
        for row in results:
            vehicles.append(cls(row))
        return vehicles

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM vehicle WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO vehicle (style, color, name, user_id) VALUES (%(style)s, %(color)s, %(name)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE vehicle SET style = %(style)s, color = %(color)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM vehicle WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)
