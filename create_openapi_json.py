import json

import os

from pathlib import Path

from fastapi.openapi.utils import get_openapi

from car_rental.api import api



def create_openapi_json() -> None:
    with open(file="docs/openapi.json", mode="w") as f:
        openapi: dict = get_openapi(
            title=api.title,
            version=api.version,
            openapi_version=api.openapi_version,
            description=api.description,
            routes=api.routes,
        )
        json.dump(obj=openapi, fp=f)


if __name__ == "__main__":
    create_openapi_json()