# CMD ?= python -m openapi_stream.jsonschema
CMD ?= python -m openapi_stream.jsonschema.codegen

OPTS ?= --log=DEBUG
# default: TARGET?=main
# default:
# 	$(MAKE) ${TARGET}
default: 00 01 02 03 04 05 06 07 08 09 10 11 main

main:
	@$(CMD) examples/separated/main.yaml ${OPTS} | tee dst/main.py
dst:
	mkdir -p dst
00: dst
	@$(CMD) examples/00*.yaml ${OPTS} | tee dst/00.py
01: dst
	@$(CMD) examples/01*.yaml ${OPTS} | tee dst/01.py
02: dst
	@$(CMD) examples/02*.yaml ${OPTS} | tee dst/02.py
03: dst
	@$(CMD) examples/03*.yaml ${OPTS} | tee dst/03.py
04: dst
	@$(CMD) examples/04*.yaml ${OPTS} | tee dst/04.py
05: dst
	@$(CMD) examples/05*.yaml ${OPTS} | tee dst/05.py
06: dst
	@$(CMD) examples/06*.yaml ${OPTS} | tee dst/06.py
07: dst
	@$(CMD) examples/07*.yaml ${OPTS} | tee dst/07.py
08: dst
	@$(CMD) examples/08*.yaml ${OPTS} | tee dst/08.py
09: dst
	@$(CMD) examples/09*.yaml ${OPTS} | tee dst/09.py
10: dst
	@$(CMD) examples/10*.yaml ${OPTS} | tee dst/10.py
11: dst
	@$(CMD) examples/11*.yaml ${OPTS} | tee dst/11.py

xxx: TARGET ?= default
xxx: CMD := python -m openapi_stream.jsonschema
xxx:
	$(MAKE) CMD="${CMD}" ${TARGET}
