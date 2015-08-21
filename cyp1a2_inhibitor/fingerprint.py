import pybel
line=0
inputfile=pybel.readfile("smi","clearance_fixpka.smiles")
outfile=open("clearance_fingerprint.txt", 'w')

num_molecule=0

for mol in inputfile:

	outfile.write(mol.title)
	outfile.write(" ")

	maccsfile = open("fp_noduplicate.smi", 'r')
	while True:
		line_maccs=maccsfile.readline()
		line=line+1
		if not line_maccs:
			break
		if line_maccs.find(":")>0:
			line_maccs=line_maccs[line_maccs.find("'")+1:line_maccs.rfind("'")]
			if len(line_maccs)>0:
				smarts = pybel.Smarts(line_maccs)
				num=smarts.findall(mol)
				
				outfile.write(str(len(num)))
				outfile.write(" ")
				
	maccsfile.close()

	outfile.write("\n")
	line=0






