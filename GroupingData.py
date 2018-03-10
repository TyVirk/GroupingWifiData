import csv
with open('wifi.csv') as f:
# Open csv file named wifi
    data = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

manfcthist = {}
# Create blank manufacturer ID Table

for row in data:
	hosp = row['SSID']
	# For every row in the data set put out the SSID column
	if 'CPH' in hosp:
	# IF CPH is in the SSID
		tmp	= row['MAC'].split(':')
		# Split the MAC column on :
		man1 = tmp[0]
		# First portion of the split
		man2 = tmp[1]
		# Second portion of the split
		man3 = tmp[2]
		# Third portion of the split
		man = man1 +':' + man2+':'+ man3
		# Re-combining 3 terms
		if man in manfcthist.keys():
			manfcthist[man] += 1
		else:
			manfcthist[man] = 1
		# Add the unique identified items to manfcthist

keys = sorted(manfcthist.keys())
# Sort results
print keys
# Print results

print '   '

import operator

sortedmanfct = sorted(manfcthist.items(), key=operator.itemgetter(1), reverse=True)
for Manufacturer, count in sortedmanfct:
	print str(Manufacturer) + ' ' + str(count)
	# Prints the Manufacturer string and the repeats in the data set
	
print '   '


tot = {}
chntot = {}

for row in data:
	mac = row['MAC']
	# Create Mac column subset
	chn = row['Channel']
	# Create Channel column subset
	comb = chn+':'+mac
	# Combine both subsets separated by :
	if comb in tot.keys():
		tot[comb] +=1
	else:
		tot[comb] =1
		
	# Count of each combination of chn and mac
		
		
lines = tot

chncount = {}
for line in lines:
	tmp1 = line.split(':')[0]
	# Split channel out from combination with mac
	tmp = int(tmp1)
	# convert to integer
	if tmp in chncount.keys():
		chncount[tmp] +=1
	else:
		chncount[tmp] =1
	# Count of each unique channel
		

keys = sorted(chncount.keys())
print keys
# Prints the unique channels

import operator

sortedaccess = sorted(chncount.items(), key=operator.itemgetter(0))
for AccessPoint, count in sortedaccess:
	print str(AccessPoint) + ' ' + str(count)
	# Prints the count of each unqiue mac on the identified channels
	
