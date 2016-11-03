import person
import unittest


class test_person(unittest.TestCase):
    def test001(self):
        a = person.person()
        # person.person.fee = '12','a'
        print a.fee
        # print 'a.__dict__:'+a.__dict__
        # print 'a.__doc__:'+a.__doc__
