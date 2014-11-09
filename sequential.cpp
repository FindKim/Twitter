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
#include <boost/unordered_map.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>
#include <sstream>

#define DEBUG

using namespace std;

void getNumberedMonth(string *toFill, string input);

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
	
	//bin width in minutes
	int BIN_WIDTH = atoi(argv[3]);
	
	//map of hashtag keys and all associated timestamps
	boost::unordered_map<string, boost::unordered_map<string, int> >  hashtags_to_map;
	
	//the current tweet we are parsing
	string current_tweet;

	//working toward the timestamp
	string created_string = "\"created_at\":";
	string whole_timestamp;
	string minute_timestamp;
	string bin_timestamp;

	//working toward finding hashtags
	string textField;

	//general indicies for loops and string work
	int temp_index;
	int end_index;
	int start_index;
	int i;

/////END DECLARING VARIABLES
	inFile.open(argv[1], ios_base::in);
	outFile.open(argv[2], ios_base::out);
	if(inFile.fail() || outFile.fail())
	{
		cout << "Either I could not open " << argv[1] << " for reading or " << argv[2] << "for writing." << endl;
		return 1;
	}

	//get a line
	getline(inFile, current_tweet);

	//while there is input file
	while(!inFile.eof())
	{
		//find the the timestamp
		temp_index = current_tweet.find(created_string) + created_string.length() + 7;
		end_index = temp_index;
		for(i = 0; i < 2; i++)
		{
			cout << "In the end_index for loop" << endl;
			end_index = current_tweet.find(":", end_index + 1);
		}			
		whole_timestamp = current_tweet.substr(temp_index, end_index-temp_index);
		
		vector<string> timestamp_parts;
		
		boost::algorithm::split(timestamp_parts, whole_timestamp, boost::algorithm::is_any_of(" "));
		
		string numbered_month;
		getNumberedMonth(&numbered_month, timestamp_parts[1]);

		minute_timestamp = timestamp_parts[2].append(" ").append(numbered_month).append(" ").append(timestamp_parts[0]).append(" ").append(timestamp_parts[3]);
		
		//we have the minute timestamp, now look for #

		//strtok(originalString) until you find "text":
			//strtok(NULL) for # or the end of text field
			//if the first character is #, "emit" the hashtag word and the new timestamp by putting them into the hashmap

		//get a line
		getline(inFile, current_tweet);
	}//end get a line loop
	
	//foreach key in the hashmap
//		cout << endl << key << ": " << endl;
		//foreach pair of timestamp, number values
//		cout <<"\t"<< timestamp << ": " << number << endl;

}	

void getNumberedMonth(string * toFill, string input)
{
	if(input == "Jan")
		*toFill = "01";
	else if(input == "Feb")
		*toFill = "02";
	else if(input == "Mar")
		*toFill = "03";
	else if(input == "Apr")
		*toFill = "04";
	else if(input == "May")
		*toFill = "05";
	else if(input == "Jun")
		*toFill = "06";
	else if(input == "Jul")
		*toFill = "07";
	else if(input == "Aug")
		*toFill = "08";
	else if(input == "Sep")
		*toFill = "09";
	else if(input == "Oct")
		*toFill = "10";
	else if(input == "Nov")
		*toFill = "11";
	else if(input == "Dec")
		*toFill = "12";
}
