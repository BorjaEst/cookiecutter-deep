"""Testing module for api metadata. This is a test file designed to use
pytest and prepared for some basic assertions and to add your own tests.

You can add new tests following the next structure:
```py
def test_{description for the test}(metadata):
    assert {statement with metadata that returns true or false}
```

The conftest.py module in the same directory includes the fixture to return
to your tests inside the argument variable `metadata` the value generated by
your function defined at `api.get_metadata`.
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


def test_authors(metadata):
    """Tests that metadata provides authors information."""
    assert "Author" in metadata
    assert metadata["Author"] == ["{{ cookiecutter.author_name }}"]


def test_authors(metadata):
    """Tests that metadata provides authors information."""
    assert "Author-email" in metadata
    assert metadata["Author-email"] == ["{{ cookiecutter.author_email }}"]


def test_description(metadata):
    """Tests that metadata provides description information."""
    assert "Description" in metadata
    assert metadata["Description"] == "{{ cookiecutter.description }}"


def test_license(metadata):
    """Tests that metadata provides license information."""
    assert "License" in metadata
    assert metadata["License"] == "{{ cookiecutter.open_source_license }}"


def test_version(metadata):
    """Tests that metadata provides version information."""
    assert "Version" in metadata
    assert isinstance(metadata["Version"], str)
    assert all(v.isnumeric() for v in metadata["Version"].split("."))
    assert len(metadata["Version"].split(".")) == 3


def test_project_url(metadata):
    """Tests that metadata provides project url information."""
    assert "Project-URL" in metadata
    assert metadata["Project-URL"] == "{{ cookiecutter.git_base_url }}"


def test_checkpoints(metadata):
    """Tests that metadata provides checkpoints information."""
    assert "Checkpoints" in metadata
    assert metadata["Checkpoints"] == []  # TODO: Add your test checkpoints
