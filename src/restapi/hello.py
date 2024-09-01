from login import login
from api import add
from common import hello
if __name__ == "__main__":
    result = login("admin", "admin")
    add_result = add(1, 2)
    hello_result = hello()
    print(result,add_result,hello_result)
