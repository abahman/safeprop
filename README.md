# CoolProp Wrappers for Safe Property Evaluation
Needed a wrapper that guaranteed outputs from CoolProp in expected format.
Also didn't want to calculate properties more than once (often occurs in a
process monitoring/real-time application).


## Features

* Replace exceptions with NaNs when they occur.
* Memoize function calls to speed up execution (at the expense of memory).


## Install for development

```bash
$ git clone git clone https://github.com/ahjortland/safeprop.git
$ cd safeprop
$ pip install --editable .
```

Requirements:

* CoolProp
* 
## TODO

* Make fluid name option variable and set at import.
* Optionally fix the cache size with FIFO buffer.
* Improve the documentation.


## License
MIT. See the [LICENSE](LICENSE) file for more details.
