from unittest.async_case import IsolatedAsyncioTestCase
from services.fake_prospects_service import FakeProspectsService


class TestFakeProspectsService(IsolatedAsyncioTestCase):

    async def test_prospects(self):
        fake_prospects_service = FakeProspectsService()
        prospects_list = await fake_prospects_service.list_prospects()
        assert len(prospects_list) == 50
        for prospect in prospects_list:
            with self.subTest(prospect=prospect["name"]):
                assert "name" in prospect and prospect["name"] is not None
                assert "mail" in prospect and prospect["mail"] is not None
                assert "phone_number" in prospect and prospect["phone_number"] is not None
