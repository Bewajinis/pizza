from api import create_app


app = create_app()


if __name__ == "__main":
    app.run(Debug=True)

