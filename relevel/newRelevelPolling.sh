#! /usr/bin/env bash

for n in {1..1000};
  do
      curl 'https://api.relevel.com/api/v2/exams/evaluation/rounds/?is_pending=True' \
        -H 'authority: api.relevel.com' \
        -H 'accept: application/json' \
        -H 'accept-language: en-GB,en;q=0.9' \
        -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3OTczNzA3LCJqdGkiOiIxZWMxNzlmZGM4YzI0YTA4YTgxYzJkMTQ1Y2RiOWVjNCIsInVzZXJfaWQiOjEyODYyN30.TU3O6f67U0GjkivLCg4elRu7rkTTwluGKbYlEjIZAlE' \
        -H 'origin: https://relevel.com' \
        -H 'platform: desktop_web' \
        -H 'referer: https://relevel.com/' \
        -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
        -H 'sec-ch-ua-mobile: ?0' \
        -H 'sec-ch-ua-platform: "macOS"' \
        -H 'sec-fetch-dest: empty' \
        -H 'sec-fetch-mode: cors' \
        -H 'sec-fetch-site: same-site' \
        -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
        --compressed
        echo  '\n'
        sleep 30
  done