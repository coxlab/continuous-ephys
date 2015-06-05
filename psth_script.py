# This is will be our scratch pad
import sys, os

from utils import pixelclock, timebase
import open_ephys
import matplotlib.pyplot as plt
import numpy as np
from get_bitcode_simple import get_bitcode_simple

# mworks
try:
    sys.path.append('/Library/Application Support/MWorks/Scripting/Python')
    import mworks.data as mw
except Exception as e:
    print("Please install mworks...")
    print e


def isiterable(o):
    return hasattr(o, '__iter__')


def sync_pixel_clock(mwk_path, oe_path, oe_channels=[0, 1]):

    # 1. read in ephys binary data and timestamps

    oe_events = open_ephys.loadEvents(oe_path)

    # unpack the channels
    channels = oe_events['channel']
    directions = oe_events['eventId'] # 0: 1 -> 0, 1: 0 -> 1
    times = oe_events['timestamps']
    event_types = oe_events['eventType']

    relevant = [ind for (ind,ch) in enumerate(channels) if ch in oe_channels]
    channels = channels[relevant]
    directions = directions[relevant]
    times = times[relevant]

    # renormalize the channel numbers to 0,1, etc...
    for i, ch in enumerate(oe_channels):
        channels[np.where(channels == ch)] = i

    # renormalize direction to 1, -1
    for i, ch in enumerate(oe_channels):
        directions[np.where(directions == 0)] = -1

    oe_codes, latencies = pixelclock.events_to_codes(np.vstack((times, channels, directions)).T, len(oe_channels), 10)

    print "OpenEphys Codes (timestamp, code, which_channel_triggered)"
    print oe_codes


    # 2, Read in mworks events
    mwk = mw.MWKFile(mwk_path)
    mwk.open()

    # Start by getting the pixel clock / bit code data
    stimulus_announces = mwk.get_events(codes=['#announceStimulus'])

    # bit_codes is a list of (time, code) tuples
    mw_codes = [(e.time, e.value['bit_code']) for e in stimulus_announces if isiterable(e.value) and 'bit_code' in e.value]

    print "MWorks Pixel Clock Codes"
    print mw_codes


    # 3. get pixel clock matches

    matches = pixelclock.match_codes(
        [evt[0] for evt in oe_codes], # oe times
        [evt[1] for evt in oe_codes], # oe codes
        [evt[0] for evt in mw_codes], # mw times
        [evt[1] for evt in mw_codes], # mw codes
        minMatch = 5,
        maxErr = 0)


    print "OE Code sequence:"
    print [evt[1] for evt in oe_codes]

    print "MW Code sequence:"
    print [evt[1] for evt in mw_codes]

    print "MATCHES:"
    print matches

    return matches



if __name__ == "__main__":

    mwk_file = sys.argv[1]
    oe_file = sys.argv[2]

    matches = sync_pixel_clock(mwk_file, oe_file, oe_channels=[3,4])

    tb = timebase.TimeBase(matches)

    # tb object lets you go back and forth between oe and mw timezones

