# This is will be our scratch pad
import sys, os
sys.path.append('/Volumes/Mac HD/Dropbox (coxlab)/Scripts/Repositories/continuous-ephys/utils')
sys.path.append('/Volumes/Mac HD/Dropbox (coxlab)/Scripts/Repositories/continuous-ephys/open-ephys analysis/')
sys.path.append('/Volumes/Mac HD/Dropbox (coxlab)/Behavior/3-port-analysis-master/')
#import mw_utils
import pixelclock
#import timebase
import OpenEphys
import matplotlib.pyplot as plt
import numpy as np
from get_bitcode_simple import get_bitcode_simple


def do_stuff():
	print("Greg does stuff")

	# 1. read in ephys binary data and timestamps

		# openEPhys code goes here
#datafile = "/Volumes/GG Data Raid/Ephys/2015-04-29_17-35-04_digitalinputtest/100_CH9_4.continuous"
#ephys_data = OpenEphys.load(datafile)
#print "length of data is: ", len(ephys_data['data'])
#print "length of timestamps is: ", len(ephys_data['timestamps'])

#plt.plot(ephys_data['data'])
#plt.show()
#"/Volumes/labuser/Desktop/EPHYS/"

eventsfile = "/Volumes/GG Data Raid/Ephys/2015-04-29_17-35-04_digitalinputtest/all_channels_4.events"
events_data = OpenEphys.load(eventsfile)

#want to give a List of 0s and 1s indicating the state of the pixel clock channels to next fnction.

#pixel_events(events_data['channel'] == 3) = 1


pixel_ch1 = [] # np.zeros((len(events_data['timestamps']),1))
pixel_ch2 =  [] #np.zeros((len(events_data['timestamps']),1))
pixel_ch1_time = [] #np.zeros((len(events_data['timestamps']),1))
pixel_ch2_time = []

counter = 0
while counter < len(events_data['timestamps']): # go thru all timestamps
	if events_data['channel'][counter] == 3:
		
		pixel_ch1.append(1)
		#pixel_ch1[counter] = 1
		pixel_ch1_time.append(events_data['timestamps'][counter])
		 
	elif events_data['channel'][counter] == 4:
		pixel_ch2.append(2)
		pixel_ch2_time.append(events_data['timestamps'][counter])
	else:
		pass

	counter += 1


"""
pixel_ch1.tolist()
pixel_ch2.tolist()
pixel_ch1 = [j for i in pixel_ch1 for j in i]
pixel_ch2 = [j for i in pixel_ch2 for j in i]
pixel_ch1 = [int(i) for i in pixel_ch1]
pixel_ch2 = [int(i) for i in pixel_ch2]
"""

#pixel_data = np.array([pixel_ch1, pixel_ch2])

"""
# make bit code from the two pixel clock channels - this is probably premature:
def f(pixel_ch1,pixel_ch2): 
	return int(str(pixel_ch1) + str(pixel_ch2),2)

ephys_bit_code = [0] * (len(pixel_ch1))
for i in range(len(pixel_ch1)):
	ephys_bit_code[i] = f(pixel_ch1[i],pixel_ch2[i])
"""


#plt.plot(events_data['timestamps'],pixel_ch2)
#plt.show()
# now we can feed in pixel_ch1 and pixel_ch2 into pixelclock.py



#matches, speed = pixelclock.process(pixel_ch1,) #input = audioFiles, mwTimes, mwCodes
 

	# 2. read in MW pixel clock data
animal_name = 'test'
session_filename = 'test_150501.mwk'
bit_code_data = get_bitcode_simple(animal_name,session_filename)
mwCodes = bit_code_data['bit_code']
mwTimes = bit_code_data['time']

#print bit_code_data['bit_code'] # this is the list of codes...


	# 3. get pixel clock matches

#matches, speed = pixelclock.process(pixel_data, mwTimes, mwCodes)

	# 4. make a timebase object


	# 5. read stim events from mw file

		# look at Javier's code

	# 6. find spikes in openephys data

	# use a simple spike sorter to start (threshold)

	# 7. plot stuff

	# probably utilities in physiology_analysis for doing this



if __name__ == "__main__":
	do_stuff()