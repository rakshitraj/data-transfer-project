# Implementing Sockets in Python

*This is the second article in Sockets in Python series. You can find the first part here.*

In the last article, we covered the basics of creating sockets in python. In this article we are going to leverage sockets and create a client-server system.

## Client

<p><a href="https://commons.wikimedia.org/wiki/File:Client-server-model.svg#/media/File:Client-server-model.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/1200px-Client-server-model.svg.png" alt="Client-server-model.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/File:Gnome-fs-client.svg" title="File:Gnome-fs-client.svg">Gnome-fs-client.svg</a>: David Vignoni
<a href="//commons.wikimedia.org/wiki/File:Gnome-fs-server.svg" title="File:Gnome-fs-server.svg">Gnome-fs-server.svg</a>: David Vignoni
derivative work: <a href="//commons.wikimedia.org/wiki/User:Calimo" title="User:Calimo">Calimo</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Calimo" title="User talk:Calimo"><span class="signature-talk">talk</span></a>) - <a href="//commons.wikimedia.org/wiki/File:Gnome-fs-client.svg" title="File:Gnome-fs-client.svg">Gnome-fs-client.svg</a>
<a href="//commons.wikimedia.org/wiki/File:Gnome-fs-server.svg" title="File:Gnome-fs-server.svg">Gnome-fs-server.svg</a>, <a href="http://www.gnu.org/licenses/lgpl.html" title="GNU Lesser General Public License">LGPL</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=15782858">Link</a></p>

A client is a piece of computer hardware or software that accesses a service made available by the server. The server is often (but not always) on another computer system, in which case the client access the service by way of a network. One or more clients may be connected to a server.

In this example we will build a **TCP Client**. A TCP Client is simply a client that uses *Transfer Control Protocol* to transmit data across the network.

There are four basic steps to creating a client application:









 

