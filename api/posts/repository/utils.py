from abc import ABC, abstractmethod



class IPost(ABC):
    @abstractmethod 
    def dict(**kwargs) -> dict: ...
 

class IPostRepository(ABC):  
    @abstractmethod
    def add(self, post: IPost) -> IPost: ...

    @abstractmethod
    def get(self, id: int) -> IPost: ...

    @abstractmethod
    def list(self, **filter_by) -> list[IPost]: ...

    @abstractmethod
    def update(self, updated_post: IPost) -> IPost: ...

    @abstractmethod
    def delete(self, id: int) -> None: ...


