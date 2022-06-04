from ..schemas.users import UserOut

# WIP

def get_user(user_id: int) -> UserOut:
    return {'user': 'from DB'}


def get_username(user_id) -> str:
    return get_user(user_id).username
