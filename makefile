IMAGE = titanic-ml

.PHONY: build run test

build:
	docker build -t $(IMAGE) .

run:
	docker run -p 5050:5000 $(IMAGE)

test:
	pytest
pathtest:
	PYTHONPATH=. pytest
