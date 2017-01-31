# JsonServer (udp-to-json-server)

Converts a UDP Stream To a HTTP Server to Json

## Getting Started

This project a simple python server that receives a UDP stream and converts it to Json using a HTTP server.
The main usage of this is to use with IoT and high level systems like Unity.

### Prerequisites

- Python 2.7 or 3.5

#### Libraries
- httpsrv
- argparse

### Installing

We use pip to install our libraries, but you can use easy_install instead.

```
pip install httpsrv
pip install argparse
```

## Running the tests

The command line output with `-h` is:

```
JSON Protocol Converter

positional arguments:
  host        UDP data stream hostname or IP (default: localhost)

optional arguments:
  -h, --help  show this help message and exit
  -p P        UDP data stream Server Port (default: 14654)
  -ph PH      HTTP JSON Server Port (default: 8000)
  -l L        Log (default: True)
  -t          Run Test Server
  -nt
```

A simple command line for test is: `python server.py localhost -p 14654 -ph 8000 -t`

To receive the HTTP data you must request `htttp://localhost:8000/`.

## Wrappers

The project has a DataLoader for Unity
You just need to attach the script with a GameObject and update the URL parameter and the pooling interval.
Also, the Wrapper has a OnUpdate event.

## Built With

* [Eclipse](https://eclipse.org/eclipse/) - Eclipse Project
* [PyDev](http://www.pydev.org/) - PyDev

## Contributing

Please read [CONTRIBUTING.md](https://github.com/rodrigomas/udp-to-json-server/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We are using SourceTree or GitHub desktop

## Authors

* **Rodrigo Marques** - [rodrigomas](https://github.com/rodrigomas)

See also the list of [contributors](https://github.com/rodrigomas/udp-to-json-server/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* None Yet




