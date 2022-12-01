current-dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL = /bin/sh

help: ## show make targets
	@awk 'BEGIN {FS = ":.*?## "} /[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

start: install ## install dependencies and create secrets
	@if [ ! -f $(current-dir).env ]; then touch .env && echo "Created .env PLEASE, FILL WITH AOC_SESSION=<SESSION>"; fi

install: ## install pipenv dependencies
	@pipenv install

calendar: ## shows current calendar or any year calendar if given parameter year=YYYY
	@pipenv run python3 aoc_calendar.py $(year)

problem: ## creates folder structure and show given problem year=yyyy and day=d
	@pipenv run python3 aoc_problem.py $(year) $(day)

today-problem: ## creates folder structure and show today's problem
	@pipenv run python3 aoc_problem.py

.PHONY: problem calendar start install help