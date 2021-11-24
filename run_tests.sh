#!/bin/bash

docker run \
    --rm \
    -v ${PWD}:/quote-extraction \
    -w /quote-extraction \
        python:3.9.5 \
            python -m unittest discover
