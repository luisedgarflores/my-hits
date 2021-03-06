from api.models.hitman import Hitman
from .utils.authorization import check_is_hitman

SUCCESS = "success"
ERRORS = "errors"
HITMEN = "hitmen"
REQUEST = "request"
CONTEXT = "context"
IS_NOT_HITMAN_ERROR = "User provided must have hitman role"


def get_hitmen(obj, info):
    try:
        is_hitman = check_is_hitman(request=info.context)

        if is_hitman:
            hitmen_from_db = Hitman.query.all()
            hitmen = map(lambda hitman: hitman.to_dict(), hitmen_from_db)
            payload = {
                SUCCESS: True,
                HITMEN: hitmen
            }
        else:
            payload = {
                SUCCESS: False,
                ERRORS: [IS_NOT_HITMAN_ERROR]
            }
    except Exception as error:
        payload = {
            SUCCESS: False,
            ERRORS: [str(error)]
        }

    return payload
