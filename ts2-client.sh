#!/bin/sh
#
# This starup script will set the correct library path
# and then startup the teamspeak binary.
#

export LD_LIBRARY_PATH=/usr/lib/ts2:$LD_LIBRARY_PATH
exec /usr/lib/ts2/TeamSpeak $*
