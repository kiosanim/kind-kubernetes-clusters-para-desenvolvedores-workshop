from unittest import IsolatedAsyncioTestCase
import requests
from app import app
from fastapi.testclient import TestClient
from app_environment import APP_ENVIRONMENT

GENERIC_HEADERS = {
    "Content-Type": "application/json"
}


client = TestClient(app)


class TestFakeProspectsAPI(IsolatedAsyncioTestCase):

    async def test_list_prospects(self):
        prospects_data = client.get(APP_ENVIRONMENT.PROSPECTS_ROUTE,
                                    headers=GENERIC_HEADERS)
        assert prospects_data.status_code == 200
        prospects_list = prospects_data.json()
        assert len(prospects_list) == 50
        for prospect in prospects_list:
            with self.subTest(prospect=prospect["name"]):
                assert prospect["name"] is not None
                assert prospect["mail"] is not None
                assert prospect["phone_number"] is not None

