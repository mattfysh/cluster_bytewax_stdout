from bytewax.dataflow import Dataflow

from bytewax.connectors.kafka import KafkaInput
from bytewax.connectors.files import FileOutput
from bytewax.connectors.stdio import StdOutput

# FAIL: this message doesn't appear
print("Running flow kafka -> fileout + stdout")

with open("/data/test.txt", "w") as file:
    # PASS: but, this does get written
    file.write("python file is running.")

flow = Dataflow()
flow.input("kafkain", KafkaInput(["redpanda:9092"], ["my_topic"]))

flow.inspect(print)  # FAIL
flow.map(lambda x: ("key", x[1].decode()))

flow.output("fileout", FileOutput("/data/out.stream"))  # PASS
flow.output("stdout", StdOutput())  # FAIL
