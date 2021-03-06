Dynamically load modules for Python
===================================

Load python module, or member of module from string.

Example Usage
-------------
Load module, or member of module from string.
::

    from dynamic_load import dynamic_load
    dattime_module =  dynamic_load("datetime") # Load datetime module
    dattime_module.datetime.now()
    time_function = dynamic_load("time.time")
    time_function()


Execute functionn of module from string.
::

    from dynamic_load import dynamic_execute
    answer =  dynamic_execute("datetime.datetime.now")
    answer = dynamic_execute("time.sleep", 10) # execute(time.sleep(10))

Convert function as string.
::

    from dynamic_load immport dynamic_string
    string = dynamic_string(datetime.datetime.now)