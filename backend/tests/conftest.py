import os

fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
fixture_files = [
    os.path.splitext(filename)[0]
    for filename in os.listdir(fixtures_dir)
    if os.path.isfile(os.path.join(fixtures_dir, filename))
]

pytest_plugins = [f"tests.fixtures.{filename}" for filename in fixture_files]
