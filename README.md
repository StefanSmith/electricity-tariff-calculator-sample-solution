# Electricity Tariff Calculator Sample Solution
This is a sample solution to an interview challenge I used to set candidates. Details of the challenge are available [here](./CHALLENGE.md).

The solution demonstrates acceptance and unit testing along with some code design practices like separation of concerns, avoidance of duplication and clear naming. It uses a ["Ports & Adapters"](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) (a.k.a "Hexagonal") architecture to separate the domain model from external concerns like displaying results and loading data. The OO domain model groups cohesive concepts and avoids accidental coupling.

## Development environment prerequisites
- python 3
- pip
- virtualenv

## Configure development environment
From project root, run:

```
virtualenv -p python3 .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

## Running the program
From project root, run:

```
python tariff_calculator/index.py input.csv
```

## Run tests
From project root, run:

```
pytest
```

## Run unit tests
From project root, run:

```
pytest test/unit
```

## Run acceptance tests
From project root, run:

```
pytest test/acceptance_test.py
```