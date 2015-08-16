import pybel
line=0
inputfile=pybel.readfile("smi","cyp2d6_fixpka.smi")
outfile=open("cyp2d6_fixpka_property.txt", 'w')

num_molecule=0

for mol in inputfile:

	outfile.write(mol.title)
	
	outfile.write(" ")
	descvalues=mol.calcdesc()
	outfile.write(str(descvalues.get('TPSA')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('HBD')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('logP')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('MW')))
	outfile.write(" ")				
	outfile.write(str(descvalues.get('tbonds')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('nF')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('bonds')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('atoms')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('HBA1')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('HBA2')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('sbonds')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('dbonds')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('MR')))
	outfile.write(" ")
	outfile.write(str(descvalues.get('abonds')))
	outfile.write(" ")
	smarts = pybel.Smarts("[+]")
	num=smarts.findall(mol)				
	outfile.write(str(len(num)))			
	outfile.write(" ")
	smarts = pybel.Smarts("[-]")
	num=smarts.findall(mol)				
	outfile.write(str(len(num)))
	outfile.write(" ")			
	

	outfile.write("\n")
	line=0






