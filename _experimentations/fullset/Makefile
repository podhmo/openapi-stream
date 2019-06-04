CMD ?= python -m openapi_stream.jsonschema.codegen

run: visitors.py data/petstore.yaml
	python main.py data/petstore.yaml

gen: visitors.py fetch

fetch: data/openapi-3.0.json data/petstore.yaml

visitors.py: data/openapi-3.0.json
	${CMD} $^ | tee $@
	black *.py

data/openapi-3.0.json:
	wget https://github.com/wework/speccy/raw/master/schemas/openapi-3.0.json -O $@
data/petstore.yaml:
	wget https://github.com/OAI/OpenAPI-Specification/raw/master/examples/v3.0/petstore-expanded.yaml -O $@

