from src.models.interface.user_repository import UserRepositoryInterface


class BalanceEditor:
    def __init__(self , user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__find_user(user_id)  # garante que o usuário existe
        self.__user_repository.edit_balance(user_id, new_balance)

        return {
            "type": "User",
            "count": 1,
            "new_balance": new_balance
        }

    def __find_user(self, user_id: int) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("User not Found")
        return user
