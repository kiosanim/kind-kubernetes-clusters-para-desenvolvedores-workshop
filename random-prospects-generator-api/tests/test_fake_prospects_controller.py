from unittest.async_case import IsolatedAsyncioTestCase
from controllers.fake_prospects_controller import FakeProspectsController


class TestFakeProspectsController(IsolatedAsyncioTestCase):

    async def test_prospects(self):
        fake_prospects_controller = FakeProspectsController()
        prospects_list = await fake_prospects_controller.generate_list_of_prospects()
        assert len(prospects_list) == 50
        for prospect in prospects_list:
            with self.subTest(prospect=prospect.name):
                assert prospect.name is not None
                assert prospect.mail is not None
                assert prospect.phone_number is not None
