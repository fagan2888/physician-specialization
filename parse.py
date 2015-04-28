import csv
import simplejson as json

#open csv file
with open('C:\Users\Desmond\Documents\GitHub\patient-viz\cms\DE1_0_2008_to_2010_Inpatient_Claims_Sample_10.csv', 'r') as csvfile:
	
	#need to create own dictionary to print in pretty format
	#insure there is a way to count frequency of diagnoisis
	
	#reads into default dictionary
	spamreader = csv.DictReader(csvfile)
	
	#printing appropriate values
	for row in spamreader:
		print(row['AT_PHYSN_NPI'], row['OP_PHYSN_NPI'], row['OT_PHYSN_NPI'], row['ICD9_DGNS_CD_1'], row['ICD9_DGNS_CD_2'], row['ICD9_DGNS_CD_3'], row['ICD9_DGNS_CD_4'], row['ICD9_DGNS_CD_5'], row['ICD9_DGNS_CD_6'], row['ICD9_DGNS_CD_7'], row['ICD9_DGNS_CD_8'], row['ICD9_DGNS_CD_9'], row['ICD9_DGNS_CD_10'])
		

	#row1 = next(spamreader)
