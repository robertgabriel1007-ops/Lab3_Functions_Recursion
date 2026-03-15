SEED_NUM = 5
FAVORITE_ARTIST = "queen"
CONTROL_NUM = max(1, SEED_NUM)


def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper


def signal_shutdown(power):

    print("Current Signal Strength:", power)

    if power == 0:
        return 1

    return 1 + signal_shutdown(power - 1)


def play_count_stream(limit):

    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2


@monitor
def run_media_engine():

    limit = CONTROL_NUM + len(FAVORITE_ARTIST)

    plays = list(play_count_stream(limit))

    print("Computed Stream Limit:", limit)
    print("Generated Play Counts:", plays)

    print("Total Plays:", sum(plays))
    print("Number of Records Processed:", len(plays))

    calls = signal_shutdown(CONTROL_NUM)

    print("Total Recursive Calls:", calls)