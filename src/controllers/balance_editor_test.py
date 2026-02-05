import pytest
from .balance_editor import BalanceEditor

user_id = 10
new_balance = 1500.0


class MockUserRepository:
    def __init__(self):
        self.balance_updated = False
        self.last_user_id = None
        self.last_balance = None

    def edit_balance(self, user_id, new_balance):
        self.balance_updated = True
        self.last_user_id = user_id
        self.last_balance = new_balance


def test_edit_balance_success():
    repo = MockUserRepository()
    balance_editor = BalanceEditor(repo)

    response = balance_editor.edit(user_id, new_balance)

    assert repo.balance_updated is True
    assert repo.last_user_id == user_id
    assert repo.last_balance == new_balance

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["new_balance"] == new_balance


def test_edit_balance_user_not_found():
    class MockUserRepositoryNotFound:
        def edit_balance(self, user_id, new_balance):
            # Simula falha ao tentar atualizar usuário inexistente
            raise Exception("User not found")

    balance_editor = BalanceEditor(MockUserRepositoryNotFound())

    with pytest.raises(Exception):
        balance_editor.edit(user_id, new_balance)
