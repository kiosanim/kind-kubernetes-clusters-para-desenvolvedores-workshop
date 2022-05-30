from fastapi import APIRouter, Response, status
from controllers.fake_prospects_controller import FakeProspectsController
from app_environment import APP_ENVIRONMENT

api_router = APIRouter()
fake_prospects_controller = FakeProspectsController()

@api_router.get(APP_ENVIRONMENT.PROSPECTS_ROUTE)
async def list_prospects(response: Response):
    prospects_list = await fake_prospects_controller.generate_list_of_prospects()
    if len(prospects_list) == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return []
    return prospects_list
