#!/usr/bin/python3

# Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
#
#     Your script should take 3 arguments: mysql username, mysql password and database name
#     You must use the module SQLAlchemy
#     You must import State and Base from model_state - from model_state import Base, State
#     Your script should connect to a MySQL server running on localhost at port 3306
#     Print the new states.id after creation
#     Your code should not be executed when imported
#
# guillaume@ubuntu:~/$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
# 6
# guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
# 1: California
# 2: Arizona
# 3: Texas
# 4: New York
# 5: Nevada
# 6: Louisiana
# guillaume@ubuntu:~/$ 
