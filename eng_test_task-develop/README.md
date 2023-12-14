
```shell
pip isntall poetry
poetry install 
playwright install
pre-commit install
```

```shell
export PYTHONPATH=.
export SIGN_IN_EMAIL=...
export SIGN_IN_PASSWORD=...
pytest --tracing on
playwright show-trace test-results/**/trace.zip
```
