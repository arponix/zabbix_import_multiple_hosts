# WHAT DOES IT !? 
# This is Zabbix_Mass_Stations automation to insert bulky information to Zabbix Server .
# It's really useful when the user wants to add lots of information such as stasions in one action, not one by one (it's really horrible one by one !)
# I prepared it and I'm sure you all know how to use it, however I want to explain very shortly and quickly for people, maybe junior  or young students.
# First of all download this file or copy/paste it in a text file and save it by any name that you want. Then Change attribute of file to executable format by the following command:
#  $ > chmod 700 Your_File_Name  
# For instance my file is zabbix_mass_stations so in the command prompt ( $ > ) I will tye this one : $ > chmod 700 zabbix_mass_stations.
# Then go to file location and run it by this command:  $ > ./Your_File_Name for my this is for instance: $ > ./zabbix_mass_stations
# the f_input for getting input file and ouput for taking output file name after running program will ask you ...
#
# It is very simple but really useful for your operation as I mentioned above. 
#
# For complete configuration , and HOW you can do it go to my Website or Youtube channel and see related videos.
# www.ARPonix.com
#
# I will share another file to clean your Text File to insert to Zabbix Server without any error, issue and difficulty.
clear

printf "Please insert your input file below... \n";
read -p 'File input: '  f_input;

printf "\n Please insert your output file below... \n";
read -p 'File Output: ' f_output;

printf "\n Please insert your output file below... \n";
read -p 'Group Name: ' f_group;

#'File Output:' ;

printf "<?xml version='1.0' encoding='UTF-8'?> \n" >> $f_output;
printf "<zabbix_export> \n" >> $f_output;
printf "\t<version>5.2</version> \n" >> $f_output;
printf "\t<date>"`date +"%Y-%m-%dT%TZ"`"</date> \n" >> $f_output;
printf "\t<groups> \n" >> $f_output;
printf "\t\t<group> \n" >> $f_output;
printf "\t\t\t<name>"$f_group"</name> \n" >> $f_output;
printf "\t\t</group> \n" >> $f_output;
printf "\t</groups> \n" >> $f_output;
printf "\t<hosts> \n" >> $f_output;

awk  -v Group=${f_group%%*( )} 'BEGIN {FS = " "} {IP=$1; hostname=$2}
	{printf "<host>\n"; 
	 printf "\t<host>"hostname"</host>\n";
	 printf "\t<name>"hostname"</name>\n";
	 printf "\t<groups>\n";
	 printf "\t<group>\n";
	 printf "\t<name>"Group"</name>\n";
	 printf "\t</group>\n";
	 printf "\t</groups>\n";
	 printf "\t<interfaces>\n";
	 printf "\t<interface>\n";
	 printf "\t<ip>"IP"</ip>";
	 printf "\t<interface_ref>if1</interface_ref>\n";
	 printf "\t</interface>\n";
	 printf "\t</interfaces>\n";
	 printf "\t<inventory_mode>DISABLED</inventory_mode>\n";
	 printf "</host>\n";    }' $f_input >>$f_output

printf "\n \t</hosts> \n" >> $f_output;
printf "</zabbix_export>  \n" >> $f_output;
