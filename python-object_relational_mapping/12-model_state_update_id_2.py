#!/usr/bin/python3

# Write a script that changes the name of a State object from the database hbtn_0e_6_usa
#
#     Your script should take 3 arguments: mysql username, mysql password and database name
#     You must use the module SQLAlchemy
#     You must import State and Base from model_state - from model_state import Base, State
#     Your script should connect to a MySQL server running on localhost at port 3306
#     Change the name of the State where id = 2 to New Mexico
#     Your code should not be executed when imported
#
# guillaume@ubuntu:~/$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
# guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
# 1: California
# 2: New Mexico
# 3: Texas
# 4: New York
# 5: Nevada
# 6: Louisiana
# guillaume@ubuntu:~/$ 
