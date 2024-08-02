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
        ":event-handler",
        "3rdparty/python#gunicorn"
    ],
    script="gunicorn",
    args=[
        "event_handler:app", 
        "-c", 
        "/conf/gunicorn.conf.py"
    ],
)



docker_image(
    name = "img",
    repository = "fourkeys/event-handler",
    dependencies = [
        ":binary",
        "common:gunicorn_conf"
    ]
)