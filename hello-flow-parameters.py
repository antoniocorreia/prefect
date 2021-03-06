import prefect
from prefect import task, Flow, Parameter

@task
def say_hello(name):
    logger = prefect.context.get("logger")
    logger.info(f"Hello, {name}!")

with Flow("hello-flow") as flow:
    # An optional parameter "people", with a default list of names
    people = Parameter("people", default=["Arthur", "Ford", "Marvin"])
    # Map `say_hello` across the list of names
    say_hello.map(people)

# Register the flow under the "tutorial" project
flow.register(project_name="tutorial")