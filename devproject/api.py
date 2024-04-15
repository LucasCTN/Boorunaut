from booru.api import router as booru_router
from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.parser import Parser
from ninja.types import DictStrAny
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI
import orjson


class ORJSONParser(Parser):
    def parse_body(self, request: HttpRequest):
        return orjson.loads(request.body)


api = NinjaExtraAPI(parser=ORJSONParser())
api.register_controllers(NinjaJWTDefaultController)
api.add_router('/', booru_router)
