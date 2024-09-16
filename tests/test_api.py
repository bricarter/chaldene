import unittest

from tests.base_testcase import BaseTestCase


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

    def test_update_resource_request(self):
        response = self.client.put(f"/api/requests/{1}", json=self.test_data[5])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "resource request updated successfully.")

        # validate duplicate requests cannot be added
        # even through an update
        response = self.client.put(f"/api/requests/{1}", json=self.test_data[5])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "that resource request already exists.")

        # invalid id
        response = self.client.put(f"/api/requests/{9}", json=self.test_data[5])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "that resource request is not available at this time.")

    def test_delete_resource_request(self):
        response = self.client.delete(f"/api/requests/{3}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "resource request deleted successfully.")

        # invalid id
        response = self.client.delete(f"/api/requests/{9}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "that resource request is not available at this time.")    




if __name__ == "__main__":
    unittest.main()
