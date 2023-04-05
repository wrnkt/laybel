run-python:
	python3 ./src/main/python/scrapelisting.py "$(URL)"

run-java:
	mvn clean install
	mvn exec:java
