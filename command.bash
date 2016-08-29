#!/bin/bash

curl -i -H "Content-Type: application/json" -X POST -d '{"cmd": "start", "opts": {"output-file": "/tmp/yardstick.out"}, "args": "../kklt/samples/ping.yaml"}' http://localhost:5000/yardstick/task/
