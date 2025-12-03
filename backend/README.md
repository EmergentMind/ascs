# Backend

## Testing

Backend tests are implemented in Pytest and stored along with the code they test. For example, the tests for route `foo`, as defined in `app/api/foo/foo.py` are located in `app/api/foo/test_foo.py` so the tested code can be easily referenced as the code-base grows.
Testing utilities are stored in `app/test_utils'

You can run all backend tests, with coverage, from `./backend` by executing `bash ./test.sh`.

