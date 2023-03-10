import asyncio

from temporalio.client import Client

from flask import Flask

# Import the workflow from the previous code
from run_worker import SayHello

app = Flask(__name__)


@app.route("/")
async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        SayHello.run, "my name", id="my-workflow-id", task_queue="my-task-queue"
    )

    return result


if __name__ == "__main__":
    asyncio.run(main())
    app.run(debug=True)
