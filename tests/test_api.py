import unittest

from . import BaseTestCase


class TestAPI(BaseTestCase):

    def test_get_resource_requests(self):
        response = self.client.get("/api/requests")
        self.assertEqual(response.status_code, 200)




if __name__ == "__main__":
    unittest.main()