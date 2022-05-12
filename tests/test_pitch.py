import unittest

from app.models import User, Pitch, Comment


class Test_Pitch(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='moh', email='mykrazy@gmail.com', password='mykrazy')
        self.new_pitch = Pitch()
        self.new_comment = Comment()

    def test_user_instance(self):
        pass

    def test_pitch_instance(self):
        pass

    def test_comment_instance(self):
        pass


if __name__ == '__main__':
    unittest.main()
