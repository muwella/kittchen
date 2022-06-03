from .models.users import UserOut

# WIP get user from DB
def get_user(user_id) -> UserOut:
    return {'user': 'from DB'}


# WIP get username from DB
def get_username(user_id) -> dict:
    # reuse get user
    username = get_user(user_id)
    # return just username?
    return {'username': 'from DB'}
