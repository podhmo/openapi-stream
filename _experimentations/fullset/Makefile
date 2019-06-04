CMD ?= python -m openapi_stream.jsonschema.codegen
TARGET ?= data/people.yaml
# TARGET ?= data/petstore.yaml

run: visitors.py ${TARGET}
	python main.py --log=DEBUG ${TARGET}
validate: node_modules/.bin/speccy
	$^ lint -v ${TARGET}

node_modules/.bin/speccy:
	npm install speccy

gen: data/openapi-3.0.json fetch
	${CMD} $< | tee visitors.py
	black *.py

fetch: data/openapi-3.0.json data/petstore.yaml

data/openapi-3.0.json:
	wget https://github.com/wework/speccy/raw/master/schemas/openapi-3.0.json -O $@
data/petstore.yaml:
	wget https://github.com/OAI/OpenAPI-Specification/raw/master/examples/v3.0/petstore-expanded.yaml -O $@

