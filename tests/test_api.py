import unittest

from . import BaseTestCase


class TestAPI(BaseTestCase):

    def test_get_resource_requests(self):
        response = self.client.get("/api/requests")
        self.assertEqual(response.status_code, 200)

    def test_get_individual_request(self):
        response = self.client.get(f"/api/requests/{2}")
        self.assertEqual(response.status_code, 200)
        
        # invalid id
        response = self.client.get(f"/api/requests/{9}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "that resource request is not available at this time.")

    def test_add_resource_request(self):
        response = self.client.post("/api/requests", json=self.test_data[4])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "resource request added successfully.")

        # validate duplicate requests cannot be added
        response = self.client.post("/api/requests", json=self.test_data[4])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "that resource request already exists.")

        # validate item was supplied
        del self.test_data[4]["item"]
        response = self.client.post("/api/requests", json=self.test_data[4])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "ERROR: item is required.")        




if __name__ == "__main__":
    unittest.main()