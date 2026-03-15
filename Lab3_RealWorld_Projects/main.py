from access_control import authorization_workflow
from media_engine import run_media_engine


def main():

    print("===== ACCESS CONTROL =====")

    decision = authorization_workflow()

    print("Final Authorization Decision:", decision)

    print("\n===== MEDIA ENGINE =====")

    run_media_engine()


if __name__ == "__main__":
    main()