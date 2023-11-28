import abc

from .repositories import Repository, T, ID
from typing import Optional, List
from rest_framework.serializers import ModelSerializer


class CRUDService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(self, identifier: ID) -> Optional[T]:
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, entity: [ModelSerializer, T]) -> T:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[T]:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_by_id(self, identifier: ID) -> None:
        raise NotImplementedError()


class DefaultCRUDService(CRUDService):
    def __init__(self, repository: Repository) -> None:
        self.repository: Repository = repository

    def find_by_id(self, identifier: ID) -> Optional[T]:
        return self.repository.find_by_id(identifier)

    def save(self, entity: [ModelSerializer, T]) -> T:
        return self.repository.save(entity)

    def find_all(self) -> List[T]:
        return self.repository.find_all()

    def delete_by_id(self, identifier: ID) -> None:
        self.repository.delete_by_id(identifier)

