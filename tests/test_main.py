import pytest


@pytest.fixture
def env_fixture(monkeypatch):
    """Simulate proper env vars"""
    monkeypatch.setenv("NEMLI_DISCORD__TOKEN", "xxx")
    monkeypatch.setenv("NEMLI_DISCORD__PREFIX", "yyy",)
    yield


# Example test
def test_stupid_import_main(env_fixture):
    from nemli import main

    assert main
