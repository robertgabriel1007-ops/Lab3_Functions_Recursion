SEED_NUM = 5
FAVORITE_ARTIST = "queen"
CONTROL_NUM = max(1, SEED_NUM)


def compute_access_level(control):
    return control * 3 + len(FAVORITE_ARTIST)


def validate_access(level):
    threshold = CONTROL_NUM * 5
    return level >= threshold


def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper


@audit_log
def authorization_workflow():

    access_level = compute_access_level(CONTROL_NUM)
    threshold = CONTROL_NUM * 5

    print("CONTROL_NUM Used:", CONTROL_NUM)
    print("FAVORITE_ARTIST Length:", len(FAVORITE_ARTIST))
    print("Computed Access Level:", access_level)
    print("Threshold Applied:", threshold)

    if validate_access(access_level):
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"