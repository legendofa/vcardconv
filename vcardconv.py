import re #import regex

contacts = open('contacts.vcf', 'r'); #open file
contacts = str(contacts.read());

contacts = re.sub(r'VERSION:2.1', r'VERSION:4.0', contacts); #change version
contacts = re.sub(r'TEL;', r'TEL;TYPE=', contacts); #change syntax
contacts = re.sub(r'TEL;TYPE=VOICE', r'TEL;TYPE=CELL', contacts); #unify mobile number tag
contacts = re.sub(r'(.*)(\r?\n\1)', r'\1\n', contacts); #remove duplicate numbers
contacts = re.sub(r';CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE', r'', contacts); #change syntax
contacts = re.sub(r'(?:\n)FN.*', r'', contacts); #remove encoding tag
contacts = re.sub(r'\n\n', r'\n', contacts); #remove newlines

res = [];
tee = 0;
contacts = contacts.splitlines();
for val in contacts: #foreach line
	buff = val;
	if re.search(r'((=(\d|A|B|C|D|E|F){2}){2,})', str(val)): #if contact info is encoded in hex
		val = re.findall(r'((=(\d|A|B|C|D|E|F){2}){2,})', str(val));
		val = [x[0] for x in val]; #get each first sublist value
		i = 0;
		while i < len(val): #convert to text foreach word
			val[i] = re.sub(r'=', r'', val[i]); #remove equals
			val[i] = bytearray.fromhex(val[i]).decode();
			if i == 0: #substitute name
				tee = re.sub(r':((=(\d|A|B|C|D|E|F){2}){2,})', ':'+val[i], buff);
			if i > 0: #substitute prename
				res.append(re.sub(r';((=(\d|A|B|C|D|E|F){2}){2,})', ';'+val[i], tee));
			i = i + 1;
	else:
		res.append(buff);
#print(res);
contacts = '\n'.join(res); #join array to string
f = open("newcontacts.vcf", "a"); #create new file
f.write(contacts);