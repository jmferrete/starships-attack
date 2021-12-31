# starships-attack
A game based in interstellar battles. Also a pet project :)

## Dependencies

* `python >= 3.6`
* `virtualenv`
* `docker`

## To set up develop environment.

```bash
$> pyton3 -m venv venv
$> . venv/bin/activate
$> dev/setup.sh
```

## To run tests (and see code documentation)

```bash
$> mamba -f documentation
```

## To run the API

```bash
$> uvicorn main:app --reload
```

API documentation is available at [localhost:8000/docs](localhost:8000/docs)