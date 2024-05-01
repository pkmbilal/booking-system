import strawberry
import typing


user_data = [
    {"id": 1, "name": "Mohammed Bilal", "email": "bilal00717@gmail.com", "phone": "0543831060"},
    {"id": 2, "name": "Ameen", "email": "ameen@gmail.com", "phone": "0544837257"},
]


@strawberry.type
class User:
    id: int
    name: str
    email: str
    phone: str


def get_users():
    users = [User(**data) for data in user_data]
    return users


@strawberry.type
class Query:
    users: typing.List[User] = strawberry.field(resolver=get_users)


schema = strawberry.Schema(query=Query)