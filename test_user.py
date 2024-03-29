import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    This is a class that will contain all the tests for the user class
    """
    def setUp(self):
        """
        This will create a new user before each test
        """
        self.new_user = User("levertco","1234")

    def test_init(self):
        """
        This will test whether the user is registered correctly
        """
        self.assertEqual(self.new_user.login,"levertco")
        self.assertEqual(self.new_user.password,"1234")

    def test_user_pass(self):
        """
        Will test whether the user exists
        """
        self.assertTrue(User.user_exists)
if __name__ == "__main__":
    unittest.main()
    
