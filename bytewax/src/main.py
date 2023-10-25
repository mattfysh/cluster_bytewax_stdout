from bytewax.dataflow import Dataflow

from bytewax.connectors.files import FileInput
from bytewax.connectors.stdio import StdOutput

print("Running flow filein -> stdout")

flow = Dataflow()
flow.input("inp", FileInput("/data/inp.stream"))
flow.inspect(print)
flow.output("stdout", StdOutput())
