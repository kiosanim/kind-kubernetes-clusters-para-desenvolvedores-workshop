from faker import Faker
from faker.providers import profile, phone_number


class FakeProspectsService:

    def __init__(self):
        self.__fake = Faker(["pt_BR"])
        self.__fake.add_provider(profile)
        self.__fake.add_provider(phone_number)

    def __generate_list(self):
        prospects_list = []
        for _ in range(50):
            prospect = self.__fake.simple_profile()
            prospect["phone_number"] = self.__fake.phone_number()
            prospects_list.append(prospect)
        return prospects_list

    async def list_prospects(self) -> list:
        return self.__generate_list()
