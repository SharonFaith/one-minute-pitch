from app.models import Pitch, User
from app import db
import unittest

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.user_Pat = User(username = 'Pat', password = 'potato', email = 'pat@ms.com')

        self.new_pitch = Pitch(category_pitch = 'general', pitch_body = 'this is a pitch', user = self.user_Pat)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.category_pitch,'general')
        self.assertEquals(self.new_pitch.pitch_body,'this is a pitch')
        self.assertEquals(self.new_pitch.user,self.user_Pat)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())> 0)

