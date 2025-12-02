#!/usr/bin/env bash
set -ex

coverage run -m pytest tests/
coverage report
