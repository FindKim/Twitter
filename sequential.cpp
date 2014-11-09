//Ryan Boccabella and Kim Ngo
//Cloud Computing CSE 40822 - Final Project
//This cpp compiles to a binary which reads in a file of tweets and writes a file.
//That file contains a list of hashtags and for each hashtag it contains pairs of time, number,
//where time is the beginning of a bin of time that is BIN_WIDTH wide and the number is the
//number of tweets containing that hashtag tweeted in that time bin i.e.
//
//  PrayForBoston: MM/DD/YY HH:00  10
//								 MM/DD/YY HH:15  27
//                  .............
//  BostonMarathon: MM/DD/YY HH:00 0
//                

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <cstring>

#define DEBUG

using namespace std;

int main(int argc, char *argv[])
{
	if(argc != 4)
	{// need binary name, file to read from, file to write to
		cout << "Usage: ./binaryName inFile.txt outFile.txt BIN_WIDTH" << endl;
		return 1;
	}

/////DECLARE VARIABLES/////////
	//get a reading stream and a writing stream
	ifstream inFile;
	ofstream outFile;
//	FILE * = fopen(argv[1], "r");
//	FILE * outFile = fopen(argv[2], "w");
	
	//bin width in minutes
	int BIN_WIDTH = atoi(argv[3]);
	
	//map of hashtag keys and all associated timestamps
	map<string, map < string, int > > hashtags_to_map;
	
	//the current tweet we are parsing
	string current_tweet;
	
	
/////END DECLARING VARIABLES
	inFile.open(argv[1], ios_base::in);
	outFile.open(argv[2], ios_base::out);
	if(inFile.fail() || outFile.fail())
	{
		cout << "Either I could not open " << argv[1] << " for reading or " << argv[2] << "for writing." << endl;
		return 1;
	}
	
	//while there is input file
	while(!inFile.fail())
	{
		//get a line, will set eofbit on infile if it hits it
		getline(inFile, current_tweet);
		
		#ifdef DEBUG
			cout << endl << current_tweet << endl;
		#endif
	}
		//strtok to the timestamp
			//manipulate the timestamp via more strtoks(NULL)
		
		//strtok(originalString) until you find "text":
			//strtok(NULL) for # or the end of text field
			//if the first character is #, "emit" the hashtag word and the new timestamp by putting them into the hashmap
	//end get a line loop
	
	//foreach key in the hashmap
//		cout << endl << key << ": " << endl;
		//foreach pair of timestamp, number values
//		cout <<"\t"<< timestamp << ": " << number << endl;
}	
