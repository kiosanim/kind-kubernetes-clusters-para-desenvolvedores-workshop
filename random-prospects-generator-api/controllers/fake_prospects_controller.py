from dtos.prospect import Prospect
from services.fake_prospects_service import FakeProspectsService


class FakeProspectsController:

    def __init__(self):
        self.__fake_prospects_service = FakeProspectsService()

    def __dict_to_prospect__(self, prospect_dict: dict):
        prospect = Prospect(name=prospect_dict["name"],
                            mail=prospect_dict["mail"],
                            phone_number=prospect_dict["phone_number"])
        return prospect

    async def generate_list_of_prospects(self):
        list_of_dict_of_prospects = await self.__fake_prospects_service.list_prospects()
        list_of_prospects = [self.__dict_to_prospect__(prospect_dict=prospect_dict)
                             for prospect_dict in list_of_dict_of_prospects]
        return list_of_prospects
