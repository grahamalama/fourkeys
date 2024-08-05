import os

import google.api_core
from google.cloud import pubsub_v1

os.environ["PUBSUB_EMULATOR_HOST"] = 'localhost:8085'

def create_topic(topic_id: str, project_id: str = "fourkeys-local") -> str:
    publisher = pubsub_v1.PublisherClient()
    with publisher:
        topic_path = publisher.topic_path(project_id, topic_id)
        try:
            topic = publisher.create_topic(request={"name": topic_path})
            print(f"Created topic: {topic.name}")
        except google.api_core.exceptions.AlreadyExists:
            print(f"Topic {topic_path} already exists")
        return topic_path

def create_push_subscription(topic_path, source, push_endpoint):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path("fourkeys-local", f"{source}-subscription")

    with subscriber:
        try:
            subscription = subscriber.create_subscription(
                request={
                    "name": subscription_path,
                    "topic": topic_path,
                    "push_config":{
                        "push_endpoint": push_endpoint
                    },
                }
            )
            print(f"created {subscription.name}")
        except google.api_core.exceptions.AlreadyExists:
            print(f"Push subscription {subscription_path} already exists")



if __name__ == "__main__":
    SOURCES = [
        ("github", "http://github-parser:8001")
    ]
    for source, push_endpoint in SOURCES:
        topic = create_topic(source)
        create_push_subscription(topic, source, push_endpoint)
