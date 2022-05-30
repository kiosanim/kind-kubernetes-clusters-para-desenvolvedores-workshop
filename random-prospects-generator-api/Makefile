NAME = fabiosartori/random-prospects-genetator-api
VERSION = 0.1.1
.PHONY: all build build-nocache
all: build
build:
	docker build -t $(NAME):$(VERSION) --rm .

build-nocache:
	docker build -t $(NAME):$(VERSION) --no-cache --rm .

push:
	docker image push $(NAME):$(VERSION)


