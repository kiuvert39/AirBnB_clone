import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init_with_kwargs(self):
        kwargs = {
            'id': '123',
            'created_at': '2023-01-15T10:30:00.000000',
            'updated_at': '2023-01-15T10:30:00.000000',
            'name': 'test_object'
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime.strptime('2023-01-15T10:30:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj.updated_at, datetime.strptime('2023-01-15T10:30:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj.name, 'test_object')

    def test_init_without_kwargs(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_method(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)
        

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

if __name__ == '__main__':
    unittest.main()
