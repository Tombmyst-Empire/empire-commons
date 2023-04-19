REQUIREMENT_FILE=requirements.txt

.venv:
    @mkdir -p venv
    python3 -m venv venv

configure: .venv
    . venv/bin/activate
    @export PYTHONPATH=$$(pwd):$$PYTHONPATH

#doc  TODO

format:
    black src
    isort src --filter-files --profile black

lint:
    pylint

cython:
    @python3 setup.py build_ext --inplace

test: configure, cython
    pip3 install -r requirements_dev.txt
    pytest --cov=src --cov-fail-under=35 -vvv

build:
    @python3 setup.py build_ext --inplace
