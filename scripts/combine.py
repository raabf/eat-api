import os
from typing import List


def main():
	if(os.path.isdir('dist')):
		os.chdir('dist')
		files: List[str] = list()

		combinedDFName: str = 'combined'
		outFileName: str = 'all.json'

		for dir in os.listdir('.'):
			if os.path.isdir(dir):
				os.chdir(dir)
				if os.path.isdir(combinedDFName):
					os.chdir(combinedDFName)
					if os.path.exists(combinedDFName + '.json'):
						files.append(os.path.join(os.getcwd(), combinedDFName + '.json'))
						print('Found ' + combinedDFName + '.json for: ' + dir)
					os.chdir('..')		
				os.chdir('..')

		with open(outFileName, 'w') as outFile:
			outFile.write('{"canteens": [\n')
			for i, f in enumerate(files):
				with open(f) as inFile:
					for line in inFile:
						outFile.write(line)
					if i < len(files) -1:
						outFile.write(',')
			outFile.write(']}')

if __name__ == "__main__":
    main()