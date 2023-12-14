#!/usr/bin/env bash

args=("$@")

case "${1}" in
    "bash")
        shift
        exec bash -c "${args[@]:1}"
        ;;
    "delay")
        exec bash -c "while true; do sleep 20; done"
        ;;
    "run")
        exec bash -c "pytest ${args[@]:1}"
        ;;
esac
