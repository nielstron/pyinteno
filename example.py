import os
import pprint
import asyncio

from pyinteno import Inteno

ROUTER_URL = os.environ.get("ROUTER_URL")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


async def local() -> None:
    """
    Placeholder test function for local testing.
    """
    assert ROUTER_URL is not None, "ROUTER_URL environment variable is not set"
    assert USERNAME is not None, "USERNAME environment variable is not set"
    assert PASSWORD is not None, "PASSWORD environment variable is not set"

    print("Testing Inteno connection...")
    print("Listing devices connected to Inteno router:")
    device = Inteno(
        url=ROUTER_URL,
        username=USERNAME,
        password=PASSWORD,
    )
    await device.ensure_logged_in()
    pprint.pprint(await device.list_devices())
    pprint.pprint(await device.hardware_info())


if __name__ == "__main__":
    if ROUTER_URL is None:
        ROUTER_URL = input("Enter Router URL (i.e. 192.168.1.1): ")
    if USERNAME is None:
        USERNAME = input("Enter Username: ")
    if PASSWORD is None:
        PASSWORD = input("Enter Password: ")

    asyncio.run(local())
