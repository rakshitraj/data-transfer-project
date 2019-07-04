# Socket

An internet socket or a network socket is the endpoint of a bidirectional inter-process communication flow across an IP based computer network, such as the internet.
A socket is therfore a thethering structure that is bi-directional, disposable and acts between two servers.

Python has built-in support for TCP sockets.

## Creating a socket

```python
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(( <host> , <port> ))
```
## Creating a socket - Code explained
```python
import socket
```
Imports the socket library from `lib/socket.py` This library contains attributes like `AF_INET`, `SOCK_STREAM` etc. and other functions like `socket()`, `connect()`, `accept()` etc.
```python
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Creates and returns the socket object `mysocket` using the `socket()` function. `socket()` takes two parameters, *Internet Address Family* and the *socket type* for the specific protocol that we are using.

`socket.AF_INET` refers to the **A**ddress **F**amily. It is a constant defined in the socket library. `AF_*` represents the various address and protocol families. Its variants include,

`AF_UNIX`

`AF_INET` internet address family for IPv4

`AF_INET6` internet address family for IPv6

`socket.SOCK_STREAM` is the socket type for TCP. This parameter is supplied to denote that TCP will be used to transport our messages in the network. `SOCK_STREAM` proides sequenced, reliable, two-way, connection-based byte-streams. Out of bounds transmission mechanism may be supported. Variants include
`SOCK_STREAM`, `SOCK_DGRAM`, `SOCK_RAW`, `SOCK_RDM`, `SOCK_SEQPACKET` etc. More constants may be available depending on the system.

`AF_*` and `SOCK_*` (address family and socket kind) constants are part of `IntEnum` collections. `IntEnum` is the base class for creating enumerated constants that are also a subclass of `int`

```python
mysocket.connect((<address>)) #address = (hostname, port)
```

The socket object is used to connect  to the given server address. The address format depends on the address family denoted by `AF_INET`. The `connect()` method connects to a remote socket at *address*.

If connection is interrupted by a signal, the `connect()` method

- waits until connection completion
- raises `socket.timeout exception` on connection timeout. `socket.timeout` is a subclass of `OSError`, raised when a timeout occurs on a socket which has had timeouts enabled via a prior call to `settimeout()` or implicitly through `setdefaulttimeout()`. The accompanying value is a string whose value is currently always "*timed out*".

`socket.connect_ex( <address> )` similar to the `connect()` method but returns an error indicator instead of raising an exception for errors returned by *C-level `connect()` call*. Other errors like *host not found* can still raise exception though. For `socket.connect_ex()`, error indicators are; 0 for successful operation and the function returns the value of `errno` variable in other cases. This method is useful in supporting *asynchronous connects*. `socket.timeout` is raised by the `connect()`method if the signal doesn't raise an exception and the socket is blocking or has a timeout. 

For non-blocking sockets, the method raises an `InterruptedError` exception if the connection is interrupted by a signal( or if the exception is raised by signal handler ). In *Python 3.5* and above, however, the method waits until connection completes instead of raising an `InterruptedError` exception if the connection is interrupted by a signal, the signal handler raises an exception and the socket is blocking or has had a timeout.
