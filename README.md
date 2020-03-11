[![Build Status](https://travis-ci.org/CIDARLAB/Cello-UCF.svg?branch=develop)](https://travis-ci.org/CIDARLAB/Cello-UCF)

# Cello UCFs

UCFs, input sensor files, and output device files are in `files/`.

# UCF JSON Schemas

Used to validate the syntax of a UCF, input sensor file, or output sensor file. Found in `schemas/`.

## Python unit tests

Validate all the files in this repository with:

	pip install -r requirements.txt
	python -m unittest

Every file in `files/` appropriately named and placed within the repository will be tested automatically by Travis CI. The matching pattern for UCF files, for example, is `files/v2/ucf/**/*.UCF.json`.

Schemas are also verified with Travis CI.

## Generating classes from JSON Schemas

### Python class

Using [json-schema-to-class](https://github.com/FebruaryBreeze/json-schema-to-class):

	json-schema-to-class gates.schema.json

### Java class

Using [jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo):

	jsonschema2pojo --source gates.schema.json --target java-gen
