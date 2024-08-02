python_sources()

python_tests(
    name="tests",
)

pex_binary(
    name = "binary",
    environment="linux",
    layout = "packed",
    execution_mode = "venv",
    include_tools = True,
    dependencies=[
        ":circleci-parser",
        "3rdparty/python#gunicorn"
    ],
    script="gunicorn",
    args=[
        "main:app", 
        "-c", 
        "/conf/gunicorn.conf.py"
    ],
)



docker_image(
    name = "img",
    repository = "fourkeys/circleci-parser",
    dependencies = [
        ":binary",
        "common:gunicorn_conf"
    ]
)