import pybel
line=0
inputfile=pybel.readfile("smi","cyp3a4_fixpka.smi")
outfile=open("cyp3a4_fixpka_property.txt", 'w')

num_molecule=0

for mol in inputfile:

	outfile.write(mol.title)
	
	outfile.write(" ")
	descvalues=mol.calcdesc()
	outfile.write(str(descvalues.get('TPSA')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('HBD')))#
	outfile.write(" ")
	outfile.write(str(descvalues.get('logP')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('MW')))
	outfile.write(" ")				
	outfile.write(str(descvalues.get('tbonds')))#
	outfile.write(" ")
	outfile.write(str(descvalues.get('nF')))#
	outfile.write(" ")
	outfile.write(str(descvalues.get('bonds')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('atoms')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('HBA1')))#
	outfile.write(" ")
	outfile.write(str(descvalues.get('HBA2')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('sbonds')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('dbonds')))#
	outfile.write(" ")
	outfile.write(str(descvalues.get('MR')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('abonds')))
	outfile.write(" ")
	maccsfile = open("MACCS.txt", 'r')
	while True:
		line_maccs=maccsfile.readline()
		line=line+1
		if not line_maccs:
			break
		if line_maccs.find(":")>0:
			line_maccs=line_maccs[line_maccs.find("'")+1:line_maccs.rfind("'")]
			if len(line_maccs)>0:
				smarts = pybel.Smarts(line_maccs)
				outfile.write(str(len(smarts.findall(mol)))+ " ")
				
	maccsfile.close()
	outfile.write("\n")	
	line=0






