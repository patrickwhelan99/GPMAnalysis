import json
import numpy
import sys

def main():
	years = {}
	artists = {}
	songs = {}
	skipped = {}
	noDesc = 0

	if len(sys.argv) > 1:
		resultsToDisplay = int(sys.argv[1])
	else:
		resultsToDisplay = 5

	with open('My Activity.json') as f:
		data = json.load(f)

		c = 0

		for x in data:
			# If not music related skip
			if not x['header'] == 'Google Play Music':
				continue

			# Years
			if x['time'][:4] in years:
				years[x['time'][:4]] = years[x['time'][:4]] + 1
			else:
				years[x['time'][:4]] = 1


			# Artists
			try:
				if x['description'] in artists:
					artists[x['description']] = artists[x['description']] + 1
				else:
					artists[x['description']] = 1

			except:
				noDesc = noDesc + 1

			# Skipped Songs
			if x['title'][:7] == 'Skipped':
				songName = x['title'][8:]
				if songName in skipped:
	                                skipped[songName] = skipped[songName] + 1
				else:
					skipped[songName] = 1

			# Listened to Songs
			else:
				songName = x['title'][12:]

				if songName in songs:
					songs[songName] = songs[songName] + 1
				else:
					songs[songName] = 1

	print("\n\n\nTop " + str(resultsToDisplay) + " songs\n------------")
	for k,v in sorted(songs.items(), key=lambda item: item[1], reverse=True)[:resultsToDisplay]:
		print(k + ":\t" + str(v))

	print("\n\n\nMost skipped songs\n------------------")
	for k,v in sorted(skipped.items(), key=lambda item: item[1], reverse=True)[:resultsToDisplay]:
		print(k + ":\t" + str(v))

	print("\n\n\nTop " + str(resultsToDisplay) + " Artists\n--------------")
	for k,v in sorted(artists.items(), key=lambda item: item[1], reverse=True)[:resultsToDisplay]:
        	print(k + ":\t" + str(v))

	print("\n\n\n# of songs listened to each year\n----------------------------------")
	for k,v in sorted(years.items(), key=lambda item: item[0]):
        	print(k + ":\t" + str(v))


	print("\n\n\n" + str(noDesc) + " Failed to process and were not counted\n")


if __name__ == "__main__":
    main()
