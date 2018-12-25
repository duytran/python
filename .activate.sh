#!/usr/bin/env bash

################################################################################################################
## ENVIRONMENTS
################################################################################################################

export PROJ_HOME=$PWD
export PROJ_NAME='python'

# .env loading in the shell
dotenv () {
  set -a
  #[ -f .env ] && . .env
  [ -f .env ] && . ./.env
  set +a
}

# Run dotenv on login
dotenv

################################################################################################################
## SCRIPTS
################################################################################################################
# This script install needed packages for the current environment
function python-install() {
    pip install -e .
}

# This script helps to run jupyter notebook
function python-serve-notebook() {
    jupyter notebook --ip="0.0.0.0"
}

function python-serve-lab() {
    open http://localhost:8888/lab
    nohup jupyter lab --ip="0.0.0.0" &
}