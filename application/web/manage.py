from app import create_app, db
from flask.cli import FlaskGroup

app = create_app()

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add()


if __name__ == "__main__":
    cli()
