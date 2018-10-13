# Multithreading in Python



Running several threads is similar to running several different programs concurrently, but with the following benefits −

Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track of where within its context it is currently running.

It can be pre-empted (interrupted)

It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.


# Multithreading in Python
This article covers the basics of multithreading in Python programming language. Just like multiprocessing, multithreading is a way of achieving multitasking. In multithreading, the concept of threads is used.

Let us first understand the concept of thread in computer architecture.

Thread

In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:

* An executable program.
* The associated data needed by the program (variables, work space, buffers, etc.)
* The execution context of the program (State of process)
A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).



In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process!

A thread contains all this information in a  Thread Control Block (TCB):

* Thread Identifier: Unique id (TID) is assigned to every new thread
* Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
* Program counter: a register which stores the address of the instruction currently being executed by thread.
* Thread state: can be running, ready, waiting, start or done.
* Thread’s register set: registers assigned to thread for computations.
* Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.



# The Threading Module
The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads than the thread module discussed in the previous section.

The threading module exposes all the methods of the thread module and provides some additional methods −

* threading.activeCount() − Returns the number of thread objects that are active.

* threading.currentThread() − Returns the number of thread objects in the caller's thread control.

* threading.enumerate() − Returns a list of all thread objects that are currently active.

In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −

* run() − The run() method is the entry point for a thread.

* start() − The start() method starts a thread by calling the run method.

* join([time]) − The join() waits for threads to terminate.

* isAlive() − The isAlive() method checks whether a thread is still executing.

* getName() − The getName() method returns the name of a thread.

* setName() − The setName() method sets the name of a thread.

Creating Thread Using Threading Module
To implement a new thread using the threading module, you have to do the following −

Define a new subclass of the Thread class.

Override the __init__(self [,args]) method to add additional arguments.

Then, override the run(self [,args]) method to implement what the thread should do when started.

Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by invoking the start(), which in turn calls run() method.

# Synchronizing Threads
The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.

The acquire(blocking) method of the new lock object is used to force threads to run synchronously. The optional blocking parameter enables you to control whether the thread waits to acquire the lock.

If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for the lock to be released.

The release() method of the new lock object is used to release the lock when it is no longer required.

# Multithreaded Priority Queue
The Queue module allows you to create a new queue object that can hold a specific number of items. There are following methods to control the Queue −

* get() − The get() removes and returns an item from the queue.

* put() − The put adds item to a queue.

* qsize() − The qsize() returns the number of items that are currently in the queue.

* empty() − The empty( ) returns True if queue is empty; otherwise, False.

* full() − the full() returns True if queue is full; otherwise, Fal


# join():
The join() method of a Thread instance is used to join the start of a thread’s execution to end of other thread’s execution such that a thread does not start running until another thread ends. If join() is called on a Thread instance, the currently running thread will block until the Thread instance has finished executing.
The join() method waits at most this much milliseconds for this thread to die. A timeout of 0 means to wait forever

* Syntax:

// waits for this thread to die.<br>
public final void join() throws InterruptedException

// waits at most this much milliseconds for this thread to die<br>
public final void join(long millis) <br>
              throws InterruptedException<br>

// waits at most milliseconds plus nanoseconds for this thread to die.<br>
The java.lang.Thread.join(long millis, int nanos)<br>
