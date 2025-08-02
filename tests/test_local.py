import os

from pyinteno import Inteno

ROUTER_URL = os.environ.get("ROUTER_URL")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

async def test_local() -> None:
    """
    Placeholder test function for local testing.
    This function is intended to be run locally to ensure that the environment is set up correctly.
    """
    assert ROUTER_URL is not None, "ROUTER_URL environment variable is not set"
    assert USERNAME is not None, "USERNAME environment variable is not set"
    assert PASSWORD is not None, "PASSWORD environment variable is not set"

    print( await Inteno(
        url=ROUTER_URL,
        username=USERNAME,
        password=PASSWORD,
    ).list_devices())

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_local())
    print("Local test completed successfully.")