from xml.etree import ElementTree
import glob
import pickle

directory = r'D:\dataset\xemay\motor11_2'
t = glob.glob(directory + '/*.xml')
t.sort()

data = []
for i in t:
	# load and parse the file
	tree = ElementTree.parse(i)
	# get the root of the document
	root = tree.getroot()
	# extract each bounding box
	boxes = list()
	for box in root.findall('.//name'):
		name = str(box.text)
		data.append(name)

with open('xemay_1_2_xml.pkl', 'wb') as fp:
	pickle.dump(data, fp)
	fp.close()
print(len(data))
print(len(t))		