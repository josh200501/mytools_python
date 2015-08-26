#!/usr/bin/env python
#coding:utf-8

from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('analysis_queue',group_id='test00',
    bootstrap_servers=['192.168.1.30:9092'],
    auto_offset_reset='smallest')


def read_message():
    for message in consumer:
        print("handle {0} message".format(message.offset))
        #print("message value: {0}".format(message.value))
        consumer.task_done(message)
        "commit, so we would not fetch this message again"
        consumer.commit()

if __name__ == '__main__':
    read_message()

