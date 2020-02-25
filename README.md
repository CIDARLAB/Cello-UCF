[![Build Status](https://travis-ci.org/CIDARLAB/Cello-UCF.svg?branch=develop)](https://travis-ci.org/CIDARLAB/Cello-UCF)

# Cello UCFs

UCFs, input sensor files, and output device files are in `files`.

# UCF JSON Schemas

Used to validate the syntex of the UCF or input / output file. Found in `schemas`.

## Python unit tests

Validate all the files in this repository with:

	python -m unittest

## Generating classes from JSON Schemas

### Python class

	pip install json-schema-to-class
	json-schema-to-class gate.schema.json
	
### Java class

	brew install jsonschema2pojo
	
Or install from <https://github.com/joelittlejohn/jsonschema2pojo/releases>.

	jsonschema2pojo --source gate.schema.json --target java-gen
