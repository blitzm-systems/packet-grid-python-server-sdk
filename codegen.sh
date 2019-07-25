#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


java -jar "$DIR/../openapi-generator-cli.jar" generate \
  -i "https://api.packetgrid.io/api/docs/server.openapi.yaml" \
  -g python \
  -o . \
  -c ./codegen-config.json
