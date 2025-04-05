import pytest
import os
import tempfile
from app import app as flask_app, db
from service.initialization_service import InitializationService


@pytest.fixture(scope="module")
def app():
    """Create a test client for the Flask application."""
    db_fd, db_path = tempfile.mkstemp()

    flask_app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    with flask_app.app_context():
        print(f"Using test database: {db_path}")
        db.drop_all()
        db.create_all()
        initializer = InitializationService()
        initializer.seed_initial_data()

    yield flask_app

    with flask_app.app_context():
        db.session.remove()
        db.drop_all()

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
