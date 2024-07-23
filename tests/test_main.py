import pytest


@pytest.fixture
def env_fixture(monkeypatch):
    """Simulate proper env vars"""
    monkeypatch.setenv("NEMLI__DISCORD__TOKEN", "xxx")
    monkeypatch.setenv("NEMLI__DISCORD__PREFIX", "yyy",)
    yield


# Example test
def test_stupid_import_main(env_fixture):
    from nemli import main

    assert main
