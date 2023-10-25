# bytewax stdout issue

* ensure docker is running

* `sh run.sh`
* observe stdout is working

* `sh run2.sh`
* observe no expected stdout appears
  * including the pure python print() in main2.py header
* observe other outputs
  * bytewax/data/test.txt
  * bytewax/data/out.stream

## init proc sigint

* while `run2.sh` is still running
* `CTRL+C` to interrupt
* note that bytewax image does not stop immediately
