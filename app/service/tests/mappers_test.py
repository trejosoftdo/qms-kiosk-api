"""API Handlers tests
"""

import unittest
from app.service.mappers import map_service_turn


class MappersTest(unittest.TestCase):
    """Service Mappers functions tests"""

    def test_map_service_turn(self):
        """map_service_turn: It maps a service turn correctly"""
        data = {
            "id": 1234,
            "customerName": "test-customer-name",
            "ticketNumber": "test-ticket-number",
            "peopleInQueue": 12,
        }
        response = map_service_turn(data)
        self.assertEqual(response.id, data["id"])
        self.assertEqual(response.customerName, data["customerName"])
        self.assertEqual(response.ticketNumber, data["ticketNumber"])
        self.assertEqual(response.peopleInQueue, data["peopleInQueue"])


if __name__ == "__main__":
    unittest.main()
