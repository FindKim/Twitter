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
#include <ctype.h>
#include <stdlib.h>
#include <algorithm>

#define DEBUG

using namespace std;

void getNumberedMonth(string *toFill, string input); 
void get_bin_timestamp(string tweet, int bin_size, string &stamp_to_fill);
int alphabetize(const void * first, const void * second);

int main(int argc, char *argv[])
{
	if(argc != 3)
	{// need binary name, file to write to
		cout << "Usage: ./binaryName outFile.txt BIN_WIDTH" << endl;
		return 1;
	}
/////DECLARE VARIABLES/////////
	//get a writing stream for output
	ofstream outFile;
	
	//bin width in minutes
	int BIN_WIDTH = atoi(argv[2]);
	if(24*60 % BIN_WIDTH != 0)
	{
		cout << "BIN_WIDTH has at best minute granularity and must divide the 1440 minutes in a day equally" << endl;
		return 1;
	}	

	//map of hashtag keys and all associated timestamps
	boost::unordered_map<string, boost::unordered_map<string, int> >  hashtags_to_maps;
	
	//the current tweet we are parsing
	string current_tweet;

	//working toward the timestamp
	string bin_timestamp;
	string first_timestamp; //file comes in in chronological order

	//working toward finding hashtags
	string text_of_tweet_string = "\"text\": \"";
	string current_hashtag;
	boost::unordered_map<string, int> temp_bin_map;

	//general indicies for loops and string work
	int temp_index;
	int end_index;
	int start_index;
	int i, j, k;

	//iterators for working through maps
	boost::unordered_map<string, boost::unordered_map<string, int> >::iterator last_hashtag;
	boost::unordered_map<string, boost::unordered_map<string, int> >::iterator tag_iter;
	boost::unordered_map<string, int>::iterator last_timestamp;
	boost::unordered_map<string, int>::iterator time_iter;

	#ifdef DEBUG
		int numTweets = 0;
	#endif

/////END DECLARING VARIABLES
	
	//open file to write to
	outFile.open(argv[1], ios_base::out);
	if(outFile.fail() || !outFile.is_open() || !outFile.good())
	{
		cout << "Could not open " << argv[1] << "for writing." << endl;
		return 1;
	}

	//get a line
	getline(cin, current_tweet);
	get_bin_timestamp(current_tweet, BIN_WIDTH, first_timestamp);
	#ifdef DEBUG
		numTweets++;
		cout << "First tweet" << endl;
	#endif

	//while there is input file
	while(getline(cin, current_tweet))
	{
		#ifdef DEBUG
			numTweets++;
			cout << "New tweet, tweet number: " << numTweets << endl;
		#endif
		get_bin_timestamp(current_tweet, BIN_WIDTH, bin_timestamp);

		//we have the appropriate bin timestamp, now look for #tags
		temp_index = current_tweet.find(text_of_tweet_string) + text_of_tweet_string.length();

		//in case the line is not a tweet (perhaps a stray \n at the end of the file)
		if(temp_index == -1)
			continue;

		//index of first character in actual tweet text
		start_index = current_tweet.find(text_of_tweet_string) + text_of_tweet_string.length();  

		//the end of the text field of the tweet
		end_index = current_tweet.find("\", \""); 
		for(i = start_index; i < end_index; i++)
		{
			if(current_tweet[i] == '#')
			{//we've got a hash tag, read the word. hashtags only use letters, numbers, and _
			 //if hashtag is last word, the end quotes on the text will end the hasthag
				for(j = i+1; isalnum(current_tweet[j]) || current_tweet[j] == '_'; j++)
				{} //makes j the end of the hashtag
				
				//strip the hashtag out
				current_hashtag = current_tweet.substr(i, j-i);
				
				//put it in lowercase
				for(k = 0; k < current_hashtag.length(); k++)
				{
					current_hashtag[k] = tolower(current_hashtag[k]);
				}
				
				i = j-1;  //skip ahead in the for loop, i will still increment at end of loop
				#ifdef DEBUG
					cout << "\tOne hashtag is: " << current_hashtag << endl;
				#endif

				//get a reference to the map of timestamp bins to counts for this hashtag
				#ifdef DEBUG
					cout << "\t\thashtags_to_maps[current_hashtag][bin_timestamp] before: " << hashtags_to_maps[current_hashtag][bin_timestamp] << endl;
				#endif
				
				//increase the count of occurrences of that hashtag in that timebin
				hashtags_to_maps[current_hashtag][bin_timestamp]++;			

				#ifdef DEBUG
					cout << "\t\thashtags_to_maps[current_hashtag][bin_timestamp] after: " << hashtags_to_maps[current_hashtag][bin_timestamp] << endl;
				#endif
			}
		}
		
	}//end get a line loop

	//save some function calls to getting the end iterator
	last_hashtag = hashtags_to_maps.end(); 
	for(tag_iter = hashtags_to_maps.begin(); tag_iter != last_hashtag; ++tag_iter)
	{//foreach key in the map (i.e. each hashtag)

		temp_bin_map = tag_iter->second; //get the value, which is another map
		last_timestamp = temp_bin_map.end(); //save more function calls
		vector<string> hashtags_timestamps;
		
		//sort into 
		for(time_iter = temp_bin_map.begin(); time_iter != last_timestamp; ++time_iter)
		{
			hashtags_timestamps.push_back(time_iter->first);
		}
							 //Y    _   M   _   D   _   T _'\0'
		const char *tstamps[hashtags_timestamps.size()];
		for(i = 0; i < hashtags_timestamps.size(); i++)
		{
			tstamps[i] = hashtags_timestamps[i].c_str();  //copy string from vector into array
			cout << "Placing " << hashtags_timestamps[i].c_str() << " into tstamps" << endl;
		}

		//sort all timestamps for this one	
		qsort(tstamps, hashtags_timestamps.size(), sizeof(char *), alphabetize);

		outFile << endl <<  "------------------------------------------------------------------------------------------" << endl << tag_iter->first << endl;
		for(i = 0; i < hashtags_timestamps.size(); i++)
		{
			outFile << "\t" << tstamps[i] << ": " << temp_bin_map[tstamps[i]] << endl;
		}
		outFile << "------------------------------------------------------------------------------------------" << endl;
	}
}	

int alphabetize(const void * first, const void * second)
{
	
	int i;
	if(first == NULL || second == NULL)
		cout << "AHHHHHHH" << endl;

	char ** f = (char **) first;
	char ** s = (char **) second;
	cout << "Comparing " << *f << " to " << *s << ": " << strcmp(*s,*f) << endl;

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

void get_bin_timestamp(string tweet, int bin_size, string &stamp_to_fill/*, bool set_zero_hour*/)
{
	static long zero_hour = 0;
	string whole_timestamp;
	string minute_timestamp;
	vector<string> timestamp_parts;
	string numbered_month;
	short minutes_from_midnight;
	short bin_minutes_from_midnight;
	vector<string> time_of_day_parts;
	short hour;
	short minute;
	short temp_index;
	short offset_index;
	short end_index;
	short i;
	string created_string = "\"created_at\":";
	char text_hour[2], text_minute[2];

	//find the the last timestamp
	while( (offset_index = tweet.find(created_string)) != -1)
	{
		temp_index = offset_index + created_string.length() + 7;  //there's some spaces and a constant length day of the week
	}

	temp_index = old_index;
	//in case there is no timestamp
	if(temp_index == created_string.length() + 6)
		return;

	end_index = temp_index;
	for(i = 0; i < 2; i++)
	{
		end_index = tweet.find(":", end_index + 1);
	}
		
	whole_timestamp = tweet.substr(temp_index, end_index-temp_index);
	#ifdef DEBUG
		cout << "\twholetimestamp = " << whole_timestamp << endl;
	#endif
	boost::algorithm::split(timestamp_parts, whole_timestamp, boost::algorithm::is_any_of(" "));
	
	//right now month is a 3 letter abbreviation
	getNumberedMonth(&numbered_month, timestamp_parts[1]);

	boost::algorithm::split(time_of_day_parts, timestamp_parts[3], boost::algorithm::is_any_of(":"));

	minutes_from_midnight = 60 * atoi(time_of_day_parts[0].c_str()) + atoi(time_of_day_parts[1].c_str()); //60 minutes per hour

	bin_minutes_from_midnight = ( minutes_from_midnight / bin_size ) * bin_size;  //leveraging integer division for the greater good

	hour = bin_minutes_from_midnight / 60;
	minute = bin_minutes_from_midnight % 60;
	if(hour < 10)
		sprintf(text_hour, "0%d", hour);
	else
		sprintf(text_hour, "%d", hour);

	if(minute < 10)
		sprintf(text_minute, "0%d", minute);
	else
		sprintf(text_minute, "%d", minute);
	
	stamp_to_fill = timestamp_parts[2].append(" ").append(numbered_month).append(" ").append(timestamp_parts[0]).append(" ").append(text_hour).append(":").append(text_minute);

	#ifdef DEBUG
		cout << "\tbintimestamp = " << stamp_to_fill << "   where bin is of size " << bin_size << endl;
	#endif
}
