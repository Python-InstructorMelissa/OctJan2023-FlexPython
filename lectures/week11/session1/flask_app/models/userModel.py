from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import animalModel
from flask_app.models import vehicleModel


class User:
    db = 'mayhem'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.animals = []
        self.vehicles = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM user WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getEmail(cls, data):
        query = 'SELECT * FROM user WHERE email = %(email)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email) VALUES (%(firstName)s, %(lastName)s, %(email)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE user SET firstName = %(firstName)s, lastName = %(lastName)s WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM user WHERE id = %(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def userAnimals(cls, data):
        query = 'SELECT * FROM user LEFT JOIN animal ON user.id = animal.user_id WHERE user.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0])
        for row in results:
            animalData = {
                'id': row['animal.id'],
                'name': row['name'],
                'species': row['species'],
                'appendage': row['appendage'],
                'createdAt': row['animal.createdAt'],
                'updatedAt': row['animal.updatedAt'],
                'user_id': row['user_id']
            }
            oneAnimal = animalModel.Animal(animalData) # oneAnimal = on row in results = 1 instance of the Animal Class
            user.animals.append(oneAnimal) # adding the animalData to the list of animals that the user has.  user.animals is the list name it is not in the database it is only in this file it is like calling self.animallist
            # user.animals.append(animalModel.Animal(oneAnimal)) # This line is the 2 above put together
        return user