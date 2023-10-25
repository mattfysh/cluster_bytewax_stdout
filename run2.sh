set -ex

# reset test data for re-runs
rm -rf bytewax/data/test.txt bytewax/data/out.stream

echo "redpanda starting..."
docker compose up -d redpanda
sleep 3

echo "publishing messages to my_topic..."
docker compose exec redpanda rpk topic create my_topic
cat messages.txt | docker compose exec -T redpanda rpk topic produce my_topic

FLOWSPEC="src.main2:flow" docker compose up --build bytewax
