"""Category API Handlers tests
"""

import unittest
from app.category.mappers import map_category, map_category_service


class MappersTest(unittest.TestCase):
    """Category Mappers functions tests"""
    def setUp(self):
        self.category_data = {
            "id": 1234,
            "name": "test-category-name",
            "description": "test-category-description",
            "iconUrl": "app://test-icon",
            "isActive": True,
            "status": {
                "id": 4321,
                "name": "test-status-name",
                "description": "test-status-description",
                "type": "CATEGORY",
                "isActive": True,
            },
        }
        self.service_data = {
            "id": 1234,
            "name": "test-category-name",
            "description": "test-category-description",
            "iconUrl": "app://test-icon",
            "isActive": True,
            "prefix": "test-prefix",
            "category": self.category_data,
            "status": {
                "id": 5432,
                "name": "test-service-status-name",
                "description": "test-service-status-description",
                "type": "SERVICE",
                "isActive": True,
            },
        }


    def test_map_category(self):
        """map_category: It maps a category correctly"""
        response = map_category(self.category_data)
        self.assertEqual(response.id, self.category_data["id"])
        self.assertEqual(response.name, self.category_data["name"])
        self.assertEqual(response.description, self.category_data["description"])
        self.assertEqual(response.iconUrl, self.category_data["iconUrl"])
        self.assertEqual(response.isActive, self.category_data["isActive"])
        self.assertEqual(response.status.id, self.category_data["status"]["id"])
        self.assertEqual(response.status.name, self.category_data["status"]["name"])
        self.assertEqual(response.status.description, self.category_data["status"]["description"])
        self.assertEqual(response.status.type, self.category_data["status"]["type"])
        self.assertEqual(response.status.isActive, self.category_data["status"]["isActive"])

    def test_map_category_service(self):
        """map_category_service: It maps a category service correctly"""
        response = map_category_service(self.service_data)
        self.assertEqual(response.id, self.service_data["id"])
        self.assertEqual(response.name, self.service_data["name"])
        self.assertEqual(response.description, self.service_data["description"])
        self.assertEqual(response.iconUrl, self.service_data["iconUrl"])
        self.assertEqual(response.isActive, self.service_data["isActive"])
        self.assertEqual(response.status.id, self.service_data["status"]["id"])
        self.assertEqual(response.status.name, self.service_data["status"]["name"])
        self.assertEqual(response.status.description, self.service_data["status"]["description"])
        self.assertEqual(response.status.type, self.service_data["status"]["type"])
        self.assertEqual(response.status.isActive, self.service_data["status"]["isActive"])
        self.assertEqual(response.category.id, self.category_data["id"])
        self.assertEqual(response.category.name, self.category_data["name"])
        self.assertEqual(response.category.description, self.category_data["description"])
        self.assertEqual(response.category.iconUrl, self.category_data["iconUrl"])
        self.assertEqual(response.category.isActive, self.category_data["isActive"])


if __name__ == "__main__":
    unittest.main()
