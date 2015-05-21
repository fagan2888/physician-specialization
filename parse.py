import csv
#import simplejson as json
import json
from collections import Counter # available in Python 2.7 and newer
phys = {}
id = {}

def getFromDict(physician_dict, atr_list):
	return reduce(lambda d, k: d[k], atr_list, physician_dict)

def setInDict(physician_dict, atr_list, value):
	getFromDict(physician_dict, atr_list[:-1]) [atr_list[-1]] = value

#open csv file
with open('C:\Users\Desmond\Documents\GitHub\patient-viz\cms\DE1_0_2008_to_2010_Inpatient_Claims_Sample_10.csv', 'r') as csvfile:
	
	#need to create own dictionary to print in pretty format
	#insure there is a way to count frequency of diagnoisis
	
	#reads into default dictionary
	reader = csv.DictReader(csvfile)

	for row in reader:
		for i in range(0, 3):
			cat = {}
			if i == 0:
				id = row['AT_PHYSN_NPI']
				cat = 'attending'
			elif i == 1:
				id = row['OP_PHYSN_NPI']
				cat = 'operating'
			elif i == 2:
				id = row['OT_PHYSN_NPI']
				cat = 'other'
			
			prefix = 'ICD9_DGNS_CD_'
			diag = {}
			if id not in phys:
				for x in range(1, 10):
					diagId = row[prefix + str(x)]
					if not diagId in diag:
						diag[diagId] = 1
					else:
						diag[diagId] += 1
			else:
				for x in range(1, 10):
					diagId = row[prefix + str(x)]
					if diagId not in id['diagnosis']:
						setInDict(phys, [id,'diagnosis', diagId], 1)
					else:
						temp = getFromDict(phys,'diagnosis', diagId]) 
						setInDict(phys, [id, 'diagnosis', diagId], ++temp)
			if id in phys and cat not in phys[id][cat]:
				phys[id]['category'].append(cat)
			if not id in phys:
				id = {'category': [cat], 'diagnosis': diag}
	csvfile.close()
				
	with open ('json_format.txt', 'wb') as jsonfile:
		for physician in phys:
			jsonfile.write(physician)
			jsonfile.write(',')
			jsonfile.write(json.dumps(phys[physician]))
			jsonfile.write('\n')
	jsonfile.close()
	



	#printing appropriate values
	#for row in spamreader:
		#print(row['AT_PHYSN_NPI'], row['OP_PHYSN_NPI'], row['OT_PHYSN_NPI'], row['ICD9_DGNS_CD_1'], row['ICD9_DGNS_CD_2'], row['ICD9_DGNS_CD_3'], row['ICD9_DGNS_CD_4'], row['ICD9_DGNS_CD_5'], row['ICD9_DGNS_CD_6'], row['ICD9_DGNS_CD_7'], row['ICD9_DGNS_CD_8'], row['ICD9_DGNS_CD_9'], row['ICD9_DGNS_CD_10'])
