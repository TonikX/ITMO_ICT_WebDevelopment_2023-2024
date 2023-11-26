import abc
from typing import Generic, TypeVar, Optional, List
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

T = TypeVar("T", bound=models.Model)
ID = TypeVar("ID")


class Repository(Generic[T, ID], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(self, identifier: ID) -> Optional[T]:
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, entity: T) -> T:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[T]:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_by_id(self, identifier: ID) -> None:
        raise NotImplementedError()

    def __getitem__(self, index: ID) -> Optional[T]:
        return self.find_by_id(index)


class ORMRepository(Repository, metaclass=abc.ABCMeta):

    model = None

    def find_by_id(self, identifier: ID) -> Optional[T]:
        try:
            return self.model.objects.get(pk=identifier)
        except ObjectDoesNotExist:
            return None

    def save(self, entity: T) -> T:
        entity.save()
        return entity

    def find_all(self) -> List[T]:
        return self.model.objects.all()

    def delete_by_id(self, identifier: ID) -> None:
        self.model.objects.get(pk=identifier).delete()
