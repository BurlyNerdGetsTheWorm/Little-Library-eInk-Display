
import time
# import homescreen.py as HomeScreen
# import displayquote.py as DisplayQuote

print("No visitors yet.")
time.sleep(1)

while True:
    # if door_switch.value:
    if True:
        print("Have a quote!")
        # Run Display Quote function
        with open("visit_count.txt", 'r+') as visit_count:
            visit_count = int(visit_count.read())
            print(f"Current Visit Count: #{visit_count}")
            visit_count += 1
            visit_count.seek(0)
            visit_count.write(visit_count)
            visit_count.truncate()
        print(f"New Visit Count: #{visit_count}")
        time.sleep(180)
        # Run Welcome Screen Function
        print(f"Welcome to the Free Little Library, visitor #{visit_count}")
    else:
        print("Still Welcome! Do Nothing")
        print("...")
        time.sleep(1)