# Backend

## Requirements
- [devenv](https://devenv.sh/) See [getting started](https://devenv.sh/getting-started/) for installation and the just run

## Environment Workflow

Dependencies are managed devenv in `devenv.nix` where you can add `pip` packages and other tools as needed.

1. In a shell, run `devenv up` to spin up the devshell and run postgres
2. In a different shell, run `fastapi dev backend/main.py` to start the FastAPI dev server.

## Backend testing

Backend tests are implemented in Pytest and stored along with the code they test. For example, the tests for route `foo`, as defined in `app/api/foo/foo.py` are located in `app/api/foo/test_foo.py` so the tested code can be easily referenced as the code-base grows.
Testing utilities are stored in `app/test_utils'

You can run all backend tests, with coverage, from `./backend` by executing `bash ./test.sh`.

