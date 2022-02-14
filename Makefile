test: 
	tox -e unit
	tox -e lint
	tox -e type-check

docss:
	tox -e generate-docs

poetry-add-reqs:
	cat requirements.txt|xargs poetry add