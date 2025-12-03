#!/usr/bin/env bash
set -ex

coverage run -m pytest app/
coverage report
