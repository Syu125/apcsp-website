#!/bin/bash
echo -e "Content-type: text/html\n\n"
echo "<h2>RPI Status</h2>"
echo "<pre>$(./rpistatus)</pre>"

