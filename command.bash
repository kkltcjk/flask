#!/bin/bash

# curl -i -H "Content-Type: application/json" -X POST -d '{"cmd": "start", "opts": {"output-file": "/tmp/yardstick.out"}, "args": "../samples/ping.yaml"}' http://localhost:5000/api/v3/yardstick/tasks/task
# curl -i -H "Content-Type: application/json" -X POST -d '{"cmd": "list"}' http://localhost:5000/api/v3/yardstick/tasks/runner/
curl -i  "http://localhost:5000/api/v3/yardstick/testresults?task_id=91e680a6-a81c-4bd6-bf37-b91a8b7a8ba9&measurement=ping"
# curl -GET 'http://192.168.23.2:8086/query?pretty=true' --data-urlencode "db=yardstick" --data-urlencode "q=SELECT * FROM ping WHERE task_id='91e680a6-a81c-4bd6-bf37-b91a8b7a8ba9'"
