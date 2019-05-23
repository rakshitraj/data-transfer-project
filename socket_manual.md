# Sockets

An internet socket or a network socket is the endpoint of a bidirectional inter-process communication flow across an IP based computer network, such as the internet.
A socket is therfore a thethering structure that is bi-directional, disposable and acts between two servers.

Python has built-in support for TCP sockets.

## Creating a socket

```python
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(( <host> , <port> ))
```
#### Code explained
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
