# Write your code here :-)
import microbit as zth

with open('data_logger.csv', "w") as tiehan_file:
    my_file.write("")
zth.compass.calibrate()
# default initiating for the write mode of my file
while True:
    with open('data_logger.csv') as tiehan_file:
        content = tiehan_file.read()
    content = content + str(mt.temperature()) + ", " + str(mt.compass.heading()) + "\n"
    with open('data_logger.csv', "w") as tiehan_file:
        tiehan_file.write(content)
    sleep(5000)
