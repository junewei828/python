"""
Question:
    Write a function that will keep retrying to check a status of a process by calling
    the function is_status_success() until the the function returns True.

    Retry 10 times and sleep 3 seconds each retry. After the 10th try raise an exception.
    Make the retry count and the sleep time keyword parameter to the function with default values.

    The function to call to check the status is writen below. The function will randomly return True or False.
    Call the function in the loop as a way of checking success status of a process.

Requirement:
    - Use while loop
    - Use counter
    - Raise an Exception
    - keyword parameter for max retry
    - keyword parameter for sleep time between retries
"""

import random
import time



def is_status_success():
    """
    Check the status of a process and return True if status is success and False if not.
    :return:
    """
    print("Checking the status of the process.")
    list_to_chose_from = [True, True, False, False, False, False, False]

    bool_to_return = random.choice(list_to_chose_from)

    return bool_to_return


def retry_with_counter_until_status_is_success(max_retry = 10, sleep_time = 3):
    is_success = False
    counter = 0
    while counter < max_retry:
        print("retry number: {}".format(counter))
        is_success = is_status_success()
        print("the success status is: {}".format(is_success))
        if is_success:
            print("the process is success")
            break
        else:
            time.sleep(sleep_time)
        counter += 1

    # if not is_success:
    else:
        raise Exception("didn't get true after trying for {} seconds".format(max_retry*sleep_time))


retry_with_counter_until_status_is_success(max_retry=2)

    # pass # < Remove the 'pass' and fill in your code here>
