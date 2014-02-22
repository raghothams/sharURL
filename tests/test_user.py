
# file to add tests for userDAO.py
import uuid
import psycopg2.extras

import sys
sys.path.append("../")
from app.DAO.userDAO import UserDAO
from app.model.user import User


def test_nose():
    assert True, "Nose success"

# test to create a user
def test_user_create():

    user = User("tester@test.com", "test123", "tester")

    user_mapper = UserDAO("LOL")
    assert user_mapper.add(user)


def test_change_password():

    user_mapper = UserDAO("LOL")
    user = user_mapper.get_by_email("tester@test.com")
    print "retrieved user id is : ",user.id
    assert user_mapper.change_password(user.email, "test123", "testing123")

def test_delete_user():

    user_mapper = UserDAO("LOL")
    user = user_mapper.get_by_email("tester@test.com")
    assert user_mapper.delete(user.id)

