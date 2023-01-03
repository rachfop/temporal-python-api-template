# Flask/FastAPI Temporal Workflow Template

This repository provides a template for setting up a Flask or FastAPI project with the Temporal SDK for durable workflows.

## Prerequisites

Before using this template, make sure you have the following tools installed:

- [Python](https://www.python.org/downloads/) (3.6 or later)
- [Temporal CLI](https://github.com/temporalio/temporal)

## Getting Started

To use this template, follow these steps:

Clone the repository:

```bash
git clone https://github.com/your-username/flask-fastapi-temporal-template.git
```

Navigate to the appropriate directory for your desired framework (either `flask` or `fast-api`).

Activate the virtual environment:

```bash
python3 -m venv venv
. venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the Temporal server:

```bash
temporal server start-dev
```

Start the Worker:

```bash
python3 run_worker.py
```

Run either Flask or Fast API:

```bash
python3 run_flask.py
python3 run_fast.py
```

Running the tests requires poe to be installed.

```bash
python -m pip install poethepoet
```

Run tests:

```bash
poe test
```

## Further Reading

- [Flask documentation](https://flask.palletsprojects.com/en/)
- [FastAPI documentation](https://fastapi.tiangolo.com)
- [Temporal documentation](https://docs.temporal.io)
