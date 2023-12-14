""" 
Practice Question 3: Database Connection Simulator

Task:
Create a function database_connection_simulator that simulates a database connection. 
The function should randomly raise either a ConnectionError or a TimeoutError. 
Implement a retry mechanism that retries the connection up to three times 
before giving up and returning an appropriate message for the type of exception raised.
"""

import random

def database_connection_simulator():
    try: 
        random.choice([0, 1])
        return 'Connected successfully'
    except ConnectionError:
        return 'Failed to connect: ConnectionError'
    except TimeoutError:
        return 'Failed to connect: TimeoutError'
    
print(database_connection_simulator())