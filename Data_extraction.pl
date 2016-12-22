#!/usr/bin/perl -w

########################################
#Ilakya Selvarajan - ML assignment
#PERL program for data extraction from webpages for Virtual doctor
#The program takes in list of weblinks, checks if the disease has symptoms linked with it and downloads the files for disease prediction
use LWP::Simple;
use XML::Simple;
use XML::Parser;
require XML::Simple;
 use Data::Dumper;
require LWP::UserAgent;
my $ua = LWP::UserAgent->new;
$ua->timeout(10);
open(OUT,">buffer.txt");   # The file where the html page is dumped
$dirtoget="paste_your_url_here.txt";  #The collection of links

  open(IMD, $dirtoget) || die("Cannot open file");
@array= <IMD>;

open(OUT2, ">symptoms.txt");
open(OUT3, ">summary.txt");
foreach $item(@array)
{
     print $item;   

    
    #$url = $item
        
    #post the URL
      $response = $ua->get($item);
	  print $response;
	  if (Dumper($response)=~m/<h2>Symptoms<\/h2>/)  #If the file contains symptoms, copy to buffer. Else, discard
	  {
	  print OUT Dumper($response);
	  }
	# my $config = XMLin($response);
	
	
 }
 
open(IN,"buffer.txt"); 
@array=<IN>;

foreach $one(@array)
{
$i=0;
	if ($one=~m/<h1 class="with-also" itemprop="name">(.*?)<\/h1>/)  #extract disease name
	{
	print OUT2 "\n",$1,"\t";
	}
	if ($one=~m/<div id="ency_summary">(.*?)<section>/) # extract summary
	{
	print OUT2 $1,"\t";
	}
		
}

for (my $i=0; $i <= scalar(@array); $i++) 
{
if($array[$i]=~m/<h2>Symptoms<\/h2><\/div><div class="section-button"><button type="submit" aria-controls="(.*?)" role="button" title="Expand\/Collapse section">/)  # extract symptoms
	{
		print OUT3 $array[$i+2];
	}
}











