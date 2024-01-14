Read iot data from CSV file and send to broker as mqtt-client
By @HiIamLala

Installation.

Require NodeJS minimum version 12, npm.

Install dependencies with npm

        $ npm install

Start application

        $ node index.js [options value]

options: 
-     -h        set High Water Mark of input stream (default 200)
-     -f        set path to input file (REQUIRE)
-     -c        set first constrainer value, sleep between each mqtt message (ms) (default 10)
                ! this value will change to fit the transmission speed.
-     -s        set expected speed. (messages per second)
-     -b        set Broker URL (default tcp://mqtt-broker)
-     -t        set topic to publish message

