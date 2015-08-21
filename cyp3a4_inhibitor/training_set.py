import pybel
line=0
inputfile=pybel.readfile("smi","bbb_training_data.smi")
outfile=open("bbb_training.txt", 'w')

num_molecule=0

for mol in inputfile:
	if mol.title[3:4]=="+":
		outfile.write("+1 ")
	else:
		outfile.write("-1 ")
	
	

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
				if (smarts.findall(mol)):
	
					outfile.write(str(line))
					outfile.write(":1 ")
				
	maccsfile.close()
	outfile.write("\n")
	line=0

