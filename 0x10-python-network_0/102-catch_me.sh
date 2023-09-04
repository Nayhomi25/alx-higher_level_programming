#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me
curl -so /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
