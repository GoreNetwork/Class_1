from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

pfs_group2_two = []
no_aes = []

for crypto_map in crypto_maps:
	aes = False
	for each in crypto_map.children:
		if "AES" in each.text:
			aes = True
	if aes == False:
		no_aes.append(crypto_map.text)
print ("Crypto maps not using AES")
for each in no_aes:
	print (each)

print ('\n')

using_group_2 = cisco_cfg.find_objects(r"set pfs group2")

print ('using group 2')
for each in using_group_2:
	print (each.parent.text)
