#! /bin/bash
TAG=$1
#FRAPPE_BRANCH=version-11
FRAPPE_BRANCH=v11.1.59
# Uses default frappe and bench master branches from github to build the docker image. Use own URLs to override.
echo "Kafka Config : '${KAFKA_CONFIG}'"
docker build --build-arg CUR_DATE=$(date +%Y-%m-%d:%H:%M:%S) --build-arg KAFKA_CONFIG='${KAFKA_CONFIG}' \
  --build-arg GIT_FRAPPE_URL=github.com/frappe/frappe.git --build-arg FRAPPE_BRANCH=${FRAPPE_BRANCH} --build-arg GIT_BENCH_URL=github.com/frappe/bench.git \
  -t dock.elasticrun.in/er-frappe11-base:${TAG} .
docker tag dock.elasticrun.in/er-frappe11-base:${TAG} dock.elasticrun.in/er-frappe11-base:${CI_COMMIT_SHORT_SHA}
