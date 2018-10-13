#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""Generic socket server classes.

This module tries to capture the various aspects of defining a server:

For socket-based servers:

- address family:
        - AF_INET{,6}: IP (Internet Protocol) sockets (default)
        - AF_UNIX: Unix domain sockets
        - others, e.g. AF_DECNET are conceivable (see <socket.h>
- socket type:
        - SOCK_STREAM (reliable stream, e.g. TCP)
        - SOCK_DGRAM (datagrams, e.g. UDP)

For request-based servers (including socket-based):

- client address verification before further looking at the request
        (This is actually a hook for any processing that needs to look
         at the request before anything else, e.g. logging)
- how to handle multiple requests:
        - synchronous (one request is handled at a time)
        - forking (each request is handled by a new process)
        - threading (each request is handled by a new thread)

The classes in this module favor the server type that is simplest to
write: a synchronous TCP/IP server.  This is bad class design, but
save some typing.  (There's also the issue that a deep class hierarchy
slows down method lookups.)

There are five classes in an inheritance diagram, four of which represent
synchronous servers of four types:

        +------------+
        | BaseServer |
        +------------+
              |
              v
        +-----------+        +------------------+
        | TCPServer |------->| UnixStreamServer |
        +-----------+        +------------------+
              |
              v
        +-----------+        +--------------------+
        | UDPServer |------->| UnixDatagramServer |
        +-----------+        +--------------------+

Note that UnixDatagramServer derives from UDPServer, not from
UnixStreamServer -- the only difference between an IP and a Unix
stream server is the address family, which is simply repeated in both
unix server classes.

Forking and threading versions of each type of server can be created
using the ForkingMixIn and ThreadingMixIn mix-in classes.  For
instance, a threading UDP server class is created as follows:

        class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

The Mix-in class must come first, since it overrides a method defined
in UDPServer! Setting the various member variables also changes
the behavior of the underlying server mechanism.

To implement a service, you must derive a class from
BaseRequestHandler and redefine its handle() method.  You can then run
various versions of the service by combining one of the server classes
with your request handler class.

The request handler class must be different for datagram or stream
services.  This can be hidden by using the request handler
subclasses StreamRequestHandler or DatagramRequestHandler.

Of course, you still have to use your head!
# 关键是服务器提供什么服务

# 内存包含状态，可以被请求修改,这是什么服务？ 不用进程，用线程？
# 例如服务器保存一个计数器counter?
For instance, it makes no sense to use a forking server if the service
contains state in memory that can be modified by requests (since the  
modifications in the child process would never reach the initial state
kept in the parent process and passed to each child).  In this case,
you can use a threading server, but you will probably have to use
locks to avoid two requests that come in nearly simultaneous to apply
conflicting changes to the server state. 

On the other hand, if you are building e.g. an HTTP server, where all
data is stored externally (e.g. in the file system), a synchronous
class will essentially render the service "deaf" while one request is
being handled -- which may be for a very long time if a client is slow
to read all the data it has requested.  Here a threading or forking
server is appropriate.

# 这又是什么服务？惰性处理？
In some cases, it may be appropriate to process part of a request
synchronously, but to finish processing in a forked child depending on
the request data.  This can be implemented by using a synchronous
server and doing an explicit fork in the request handler class
handle() method.

# 同时处理好多请求，长链接,select, 流服务
Another approach to handling multiple simultaneous requests in an
environment that supports neither threads nor fork (or where these are
too expensive or inappropriate for the service) is to maintain an
explicit table of partially finished requests and to use select() to
decide which request to work on next (or whether to handle a new
incoming request).  This is particularly important for stream services
where each client can potentially be connected for a long time (if
threads or subprocesses cannot be used). 

Future work:
- Standard classes for Sun RPC (which uses either UDP or TCP)  # RPC服务
- Standard mix-in classes to implement various authentication
  and encryption schemes # 认证和加密的mix-in
- Standard framework for select-based multiplexing  # 基于select的多路复用

XXX Open problems:
- What to do with out-of-band data?

BaseServer:
- split generic "request" functionality out into BaseServer class.
  Copyright (C) 2000  Luke Kenneth Casson Leighton <lkcl@samba.org>

  example: read entries from a SQL database (requires overriding
  get_request() to return a table entry from the database).
  entry is processed by a RequestHandlerClass.

"""

# Author of the BaseServer patch: Luke Kenneth Casson Leighton

# XXX Warning!
# There is a test suite for this module, but it cannot be run by the
# standard regression test.
# To run it manually, run Lib/test/test_socketserver.py.

__version__ = "0.4"


import socket
import select
import sys
import os
import errno
try:
    import threading
except ImportError:
    import dummy_threading as threading

__all__ = ["TCPServer","UDPServer","ForkingUDPServer","ForkingTCPServer",
           "ThreadingUDPServer","ThreadingTCPServer","BaseRequestHandler",
           "StreamRequestHandler","DatagramRequestHandler",
           "ThreadingMixIn", "ForkingMixIn"]
if hasattr(socket, "AF_UNIX"):
    __all__.extend(["UnixStreamServer","UnixDatagramServer",
                    "ThreadingUnixStreamServer",
                    "ThreadingUnixDatagramServer"])

def _eintr_retry(func, *args):
    """restart a system call interrupted by EINTR"""
    # 重启被中断打断的系统服务
    while True:
        try:
            return func(*args)
        except (OSError, select.error) as e:
            if e.args[0] != errno.EINTR:   # 非EINTR异常，则抛出异常，不再重启
                raise

# ------------------------------------------------------------
# I. 框架基础部分
# 服务器基础框架,提供主循环和处理请求流程的功能
# *important(承上启下): get_request,(process_request),finish_request

class BaseServer:

    """Base class for server classes.

    # 用户外部接口
    Methods for the caller: 
    - __init__(server_address, RequestHandlerClass)
    - serve_forever(poll_interval=0.5)
    - shutdown()
    - fileno() -> int   # for select()
    -------------------
    - handle_request()  # if you do not use serve_forever()

    Methods that may be overridden: 
    - server_bind()
    - server_activate()
    - get_request() -> request, client_address  
    - handle_timeout()
    - verify_request(request, client_address)
    - server_close()
    - process_request(request, client_address)
    - shutdown_request(request)
    - close_request(request)
    - handle_error()

    Methods for derived classes:  # request最终处理
    - finish_request(request, client_address)

    Class variables that may be overridden by derived classes or
    instances:
    - timeout
    - address_family
    - socket_type
    - allow_reuse_address

    Instance variables:
    - RequestHandlerClass
    - socket

    """

    timeout = None

    def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()   #服务器实例保持一个Envent变量
        self.__shutdown_request = False

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        pass

    # 最好自己占用一个线程
    def serve_forever(self, poll_interval=0.5):
        """Handle one request at a time until shutdown.

        Polls for shutdown every poll_interval seconds. Ignores
        self.timeout. If you need to do periodic tasks, do them in
        another thread.
        """
        self.__is_shut_down.clear()
        try:
            while not self.__shutdown_request:  #main loop
                # XXX: Consider using another file descriptor or
                # connecting to the socket to wake this up instead of
                # polling. Polling reduces our responsiveness to a
                # shutdown request and wastes cpu at all other times.
                r, w, e = _eintr_retry(select.select, [self], [], [],  # select?
                                       poll_interval)
                if self in r:
                    self._handle_request_noblock()
        finally:
            self.__shutdown_request = False  #重置 
            self.__is_shut_down.set()  

    # 在另一线程中杀死loop线程
    def shutdown(self):
        """Stops the serve_forever loop.

        Blocks until the loop has finished. This must be called while
        serve_forever() is running in another thread, or it will
        deadlock.
        """
        # 必须在另一个线程调用shutdown
        self.__shutdown_request = True
        self.__is_shut_down.wait()

    # The distinction between handling, getting, processing and
    # finishing a request is fairly arbitrary.  Remember:
    #
    # - handle_request() is the top-level call.  It calls
    #   select, get_request(), verify_request() and process_request()
    # - get_request() is different for stream or datagram sockets
    # - process_request() is the place that may fork a new process
    #   or create a new thread to finish the request
    # - finish_request() instantiates the request handler class;
    #   this constructor will handle the request all by itself
    #  业务处理部分

    # 也可以在这里启动server
    def handle_request(self):
        """Handle one request, possibly blocking.

        Respects self.timeout.
        """
        # Support people who used socket.settimeout() to escape
        # handle_request before self.timeout was available.
        timeout = self.socket.gettimeout()  # 自己通过socket设置的超时
        if timeout is None:
            timeout = self.timeout  #类默认定义的超时
        elif self.timeout is not None:
            timeout = min(timeout, self.timeout)
        fd_sets = _eintr_retry(select.select, [self], [], [], timeout) 
        if not fd_sets[0]:
            self.handle_timeout() #处理超时
            return
        self._handle_request_noblock()

    # 非阻塞处理请求
    def _handle_request_noblock(self):
        """Handle one request, without blocking.

        I assume that select.select has returned that the socket is
        readable before this function was called, so there should be
        no risk of blocking in get_request().
        """
        try:
            request, client_address = self.get_request()  # return client sock
        except socket.error:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)  
                self.shutdown_request(request)

    def handle_timeout(self):
        """Called if no new request arrives within self.timeout.

        Overridden by ForkingMixIn.
        """
        pass

    def verify_request(self, request, client_address):
        """Verify the request.  May be overridden.

        Return True if we should proceed with this request.

        """
        return True

    def process_request(self, request, client_address):
        """Call finish_request.
        Mix-in要实现的方法

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        pass

    # 以客户端sock初始化处理器,与业务处理部分承接了
    def finish_request(self, request, client_address):  
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

    # 关闭客户端sock
    def shutdown_request(self, request):
        """Called to shutdown and close an individual request.""" 
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        pass

    def handle_error(self, request, client_address): 
        """Handle an error gracefully.  May be overridden.

        The default is to print a traceback and continue.

        """
        print '-'*40
        print 'Exception happened during processing of request from',
        print client_address
        import traceback
        traceback.print_exc() # XXX But this goes to stderr!
        print '-'*40


# ------------------------------------------------------------
# II. TCP/UDP框架部分 
# 提供TCP/UDP服务器框架初始化和基本处理流程
# TCP/UDP的主要不同是get_request的处理不同

class TCPServer(BaseServer):

    """Base class for various socket-based server classes.

    Defaults to synchronous IP stream (i.e., TCP).

    Methods for the caller:

    # 外部用户接口
    - __init__(server_address, RequestHandlerClass, bind_and_activate=True)
    - serve_forever(poll_interval=0.5)
    - shutdown()
    - fileno() -> int   # for select()
    ------------
    - handle_request()  # if you don't use serve_forever()

    Methods that may be overridden: 
    # 实例方法
    - server_bind()
    - server_activate()
    - get_request() -> request, client_address
    - handle_timeout()
    - verify_request(request, client_address)
    - process_request(request, client_address)
    - shutdown_request(request)
    - close_request(request)
    - handle_error()

    Methods for derived classes:
    
    - 下一层待实现方法
    - finish_request(request, client_address)

    Class variables that may be overridden by derived classes or
    instances:

    # 类属性
    - timeout
    - address_family
    - socket_type
    - request_queue_size (only for stream sockets)
    - allow_reuse_address

    Instance variables:

    # 实例属性
    - server_address
    - RequestHandlerClass
    - socket  比Base多了一个

    """

    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    request_queue_size = 5

    allow_reuse_address = False

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        BaseServer.__init__(self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        """Called by constructor to bind the socket.

        May be overridden.

        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()  # 多此一举？

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        self.socket.listen(self.request_queue_size) 

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        self.socket.close() #关闭主套接字

    def fileno(self):
        """Return socket file number.

        Interface required by select().

        """
        return self.socket.fileno()

    def get_request(self): # 与UDP不同
        """Get the request and client address from the socket.

        May be overridden.

        """
        return self.socket.accept()

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        try:
            #explicitly shutdown.  socket.close() merely releases
            #the socket and waits for GC to perform the actual close.
            # 关闭读写
            request.shutdown(socket.SHUT_WR)
        except socket.error:
            pass #some platforms may raise ENOTCONN here
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        # 释放socket后，等待gc清理
        request.close()


class UDPServer(TCPServer):

    """UDP server class."""

    allow_reuse_address = False

    socket_type = socket.SOCK_DGRAM

    max_packet_size = 8192

    # 面向非连接
    def get_request(self):   # 与TCP协议的处理不同
        data, client_addr = self.socket.recvfrom(self.max_packet_size)
        return (data, self.socket), client_addr

    def server_activate(self):
        # No need to call listen() for UDP.
        pass

    def shutdown_request(self, request):
        # No need to shutdown anything.
        self.close_request(request)

    def close_request(self, request):
        # No need to close anything.
        pass


# ------------------------------------------------------------
# III. 请求与主控制分裂部分
# 对得到的client sock/(data, self.sock)不同的方式进行的处理
# !对process_request的不同覆盖

class ForkingMixIn:

    """Mix-in class to handle each request in a new process."""

    timeout = 300
    active_children = None
    max_children = 40

    # self(服务器进程)清理僵尸子进程,必须处理
    def collect_children(self):
        """Internal routine to wait for children that have exited."""
        if self.active_children is None:
            return

        # If we're above the max number of children, wait and reap them until
        # we go back below threshold. Note that we use waitpid(-1) below to be
        # able to collect children in size(<defunct children>) syscalls instead
        # of size(<children>): the downside is that this might reap children
        # which we didn't spawn, which is why we only resort to this when we're
        # above max_children.
        while len(self.active_children) >= self.max_children:
            try:
                pid, _ = os.waitpid(-1, 0)  # 这一步怎么理解？
                self.active_children.discard(pid)
            except OSError as e:
                if e.errno == errno.ECHILD:
                    # we don't have any children, we're done
                    self.active_children.clear()
                elif e.errno != errno.EINTR:
                    break

        # Now reap all defunct children.
        for pid in self.active_children.copy():
            try:
                pid, _ = os.waitpid(pid, os.WNOHANG)  # 不挂起
                # if the child hasn't exited yet, pid will be 0 and ignored by
                # discard() below
                self.active_children.discard(pid)
            except OSError as e:
                if e.errno == errno.ECHILD:
                    # someone else reaped it
                    self.active_children.discard(pid)

    def handle_timeout(self):
        """Wait for zombies after self.timeout seconds of inactivity.

        May be extended, do not override.
        """
        self.collect_children()

    def process_request(self, request, client_address):
        """Fork a new subprocess to process the request."""
        self.collect_children()
        pid = os.fork()
        if pid:
            # Parent process
            if self.active_children is None:
                self.active_children = set()
            self.active_children.add(pid)
            # 父进程中关闭对request的引用
            self.close_request(request) #close handle in parent process
            return  #继续loop去
        else:
            # Child process.
            # This must never return, hence os._exit()!
            try:
                self.finish_request(request, client_address) #实例化request
                self.shutdown_request(request)
                os._exit(0)
            except:
                try:
                    self.handle_error(request, client_address)
                    self.shutdown_request(request)
                finally:
                    os._exit(1)


class ThreadingMixIn:
    """Mix-in class to handle each request in a new thread."""

    # Decides how threads will act upon termination of the
    # main process
    daemon_threads = False   # 类变量，控制是否为后台进程

    def process_request_thread(self, request, client_address):
        """Same as in BaseServer but as a thread.

        In addition, exception handling is done here.

        """
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        t = threading.Thread(target = self.process_request_thread,
                             args = (request, client_address))
        t.daemon = self.daemon_threads
        t.start()


class ForkingUDPServer(ForkingMixIn, UDPServer): pass
class ForkingTCPServer(ForkingMixIn, TCPServer): pass

class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass
class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass

if hasattr(socket, 'AF_UNIX'):

    class UnixStreamServer(TCPServer):
        address_family = socket.AF_UNIX

    class UnixDatagramServer(UDPServer):
        address_family = socket.AF_UNIX

    class ThreadingUnixStreamServer(ThreadingMixIn, UnixStreamServer): pass

    class ThreadingUnixDatagramServer(ThreadingMixIn, UnixDatagramServer): pass


# ------------------------------------------------------------
# III. 请求处理部分,业务
# finish_request(request, client_adress)

# 一实例化就开始运行处理
class BaseRequestHandler:  

    """Base class for request handler classes.

    This class is instantiated for each request to be handled.  The
    constructor sets the instance variables request, client_address
    and server, and then calls the handle() method.  To implement a
    specific service, all you need to do is to derive a class which
    defines a handle() method.

    The handle() method can find the request as self.request, the
    client address as self.client_address, and the server (in case it
    needs access to per-server information) as self.server.  Since a
    separate instance is created for each request, the handle() method
    can define arbitrary other instance variariables.

    """

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()   # 接下来的业务部分，实现handle
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass


# The following two classes make it possible to use the same service
# class for stream or datagram servers.
# Each class sets up these instance variables:
# - rfile: a file object from which receives the request is read
# - wfile: a file object to which the reply is written
# When the handle() method returns, wfile is flushed properly


class StreamRequestHandler(BaseRequestHandler):

    """Define self.rfile and self.wfile for stream sockets."""

    # Default buffer sizes for rfile, wfile.
    # We default rfile to buffered because otherwise it could be
    # really slow for large data (a getc() call per byte); we make
    # wfile unbuffered because (a) often after a write() we want to
    # read and we need to flush the line; (b) big writes to unbuffered
    # files are typically optimized by stdio even when big reads
    # aren't.
    rbufsize = -1 #缓存
    wbufsize = 0  #不缓存

    # A timeout to apply to the request socket, if not None.
    timeout = None

    # Disable nagle algorithm for this socket, if True.
    # Use only when wbufsize != 0, to avoid small packets.
    disable_nagle_algorithm = False

    def setup(self):
        self.connection = self.request
        if self.timeout is not None:
            self.connection.settimeout(self.timeout)
        if self.disable_nagle_algorithm:
            self.connection.setsockopt(socket.IPPROTO_TCP,
                                       socket.TCP_NODELAY, True)

        # 两个读写接口,可以进一步被下一层类的handle方法处理
        self.rfile = self.connection.makefile('rb', self.rbufsize) #有缓存
        self.wfile = self.connection.makefile('wb', self.wbufsize)

    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
            except socket.error:
                # An final socket error may have occurred here, such as
                # the local error ECONNABORTED.
                pass
        self.wfile.close()
        self.rfile.close()


class DatagramRequestHandler(BaseRequestHandler):

    # XXX Regrettably, I cannot get this working on Linux;
    # s.recvfrom() doesn't return a meaningful client address.

    """Define self.rfile and self.wfile for datagram sockets."""

    def setup(self):
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO
        self.packet, self.socket = self.request
        self.rfile = StringIO(self.packet)
        self.wfile = StringIO()

    def finish(self):
        self.socket.sendto(self.wfile.getvalue(), self.client_address)
