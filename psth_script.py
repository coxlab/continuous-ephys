# This is will be our scratch pad
import sys, os
sys.path.append('/Volumes/Mac HD/Dropbox (coxlab)/Scripts/Repositories/continuous-ephys/utils')
sys.path.append('/Volumes/Mac HD/Dropbox (coxlab)/Scripts/Repositories/continuous-ephys/open-ephys analysis/')
#import mw_utils
#import pixelclock
#import timebase
import OpenEphys
import matplotlib.pyplot as plt


def do_stuff():
	print("Greg does stuff")

	# 1. read in ephys binary data and timestamps

		# openEPhys code goes here
datafile = "/Volumes/GG Data Raid/Ephys/2015-04-29_17-35-04_digitalinputtest/100_CH9_4.continuous"
ephys_data = OpenEphys.load(datafile)
print "length of data is: ", len(ephys_data['data'])
print "length of timestamps is: ", len(ephys_data['timestamps'])
#plt.plot(ephys_data['data'])
#plt.show()
#"/Volumes/labuser/Desktop/EPHYS/"
eventsfile = "/Volumes/GG Data Raid/Ephys/2015-04-29_17-35-04_digitalinputtest/all_channels_3.events"
events_data = OpenEphys.load(eventsfile)
# this will be a [#number of events x 1] vector with integer entries; want to turn it into matrix by channel number:

#print "length of digital data is: ", len(events_data['channel'])
#print "length of digital timestamps is: ", len(events_data['timestamps'])
plt.plot(events_data['channel'])
plt.show()
#print events_data['channel']










	# 2. read in MW pixel clock data


	# 3. get pixel clock matches

	# 4. make a timebase object


	# 5. read stim events from mw file

		# look at Javier's code

	# 6. find spikes in openephys data

	# use a simple spike sorter to start (threshold)

	# 7. plot stuff

	# probably utilities in physiology_analysis for doing this



if __name__ == "__main__":
	do_stuff()