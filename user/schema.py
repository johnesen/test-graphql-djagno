import graphene
from graphene_django import DjangoObjectType
from graphene_django.types import DjangoObjectType

from user.models import User


def get_users():
    return User.objects.all()


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Query(graphene.ObjectType):
    users = graphene.List(UserNode)

    def resolve_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
