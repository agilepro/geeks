#!/usr/bin/perl -w 
require "cgi-lib2.pl";
#require "cookie.pl";
require "DB_communication.pl";
use CGI qw(:standard);
use DBI;
use integer;

################################################################################
$VERSION="order.cgi v1.1"; #November 10, 2001 Chris Lindstrom
#
#-------------------------------------------------------------------------------
# This script and others part of PIPC CS327 project UI
#
# Trial - user logs in and their customer ID sent to them as a cookie
# 
#
#
################################################################################

#------------------------------------------------------------------------------#
#- Main Program ---------------------------------------------------------------#
&ReadParse; #parse incoming 
print "Content-type: text/html\n\n";
print "<HTML><HEAD><TITLE>Atheist Trivia : $in{question}</TITLE></HEAD>
<BODY BGCOLOR=FFFFCC>\n";

if ( ($in{submission} eq "Vote!") && $in{poll} ne "")
{  print "Thanks for voting\n"; 
	@stats=&vote($in{table_name},$in{poll});}
else #just get results
{  @stats=&reviewResults($in{table_name}); } 

$sum=$stats[0]+$stats[1]+$stats[2]+$stats[3]+$stats[4];
@percentages= ($stats[0]*100/$sum,
		   $stats[1]*100/$sum,
		   $stats[2]*100/$sum,
		   $stats[3]*100/$sum,
		   $stats[4]*100/$sum );

@sizes=($percentages[0]*5,
	  $percentages[1]*5,
	  $percentages[2]*5,
	  $percentages[3]*5,
	  $percentages[4]*5);

#---Create output web page and hand to HTTP server

print <<EOF;


<TABLE WIDTH=468 CELLSPACING=0 CELLPADDING=10 BGCOLOR="FFFFCC" BORDER="0" BORDERCOLOR="CCCCCC" ALIGN="CENTER">
  <TR> 
    <TD BGCOLOR=0000FF ALIGN=center><FONT FACE="verdana,arial,sans-serif" COLOR="FFFFFF" SIZE=2><B>Atheist Trivia</B><BR></FONT></TD>
  </TR>
  <TR> 
    <TD><FONT FACE="verdana,arial,sans-serif" 
		COLOR="000000" SIZE=2><B>$in{question}</B><BR>
      </FONT> 
      <TABLE BORDER=0 ALIGN="CENTER" WIDTH=400>
				<TR>          <TD VALIGN=top WIDTH=50% NOWRAP><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$in{s1} </FONT></TD>
          <TD VALIGN=MIDDLE NOWRAP ALIGN=RIGHT><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$percentages[0]%</FONT></TD>
					<TD VALIGN=MIDDLE ALIGN=LEFT><TABLE CELLSPACING=0 CELLPADDING=0 CELLSPACING=0 BORDER=0><TR><TD><IMG SRC=http://www.godlessgeeks.com/IMAGES/blue_bar.GIF WIDTH=$sizes[0] HEIGHT=20></TD></TR></TABLE></TD>
        </TR>
<TR>          <TD VALIGN=top WIDTH=50% NOWRAP><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$in{s2}</FONT></TD>
          <TD VALIGN=MIDDLE NOWRAP ALIGN=RIGHT><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$percentages[1]%</FONT></TD>
					<TD VALIGN=MIDDLE ALIGN=LEFT><TABLE CELLSPACING=0 CELLPADDING=0 CELLSPACING=0 BORDER=0><TR><TD><IMG SRC=http://www.godlessgeeks.com/IMAGES/blue_bar.GIF WIDTH=$sizes[1] HEIGHT=20></TD></TR></TABLE></TD>
        </TR>
<TR>          <TD VALIGN=top WIDTH=50% NOWRAP><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$in{s3} </FONT></TD>
          <TD VALIGN=MIDDLE NOWRAP ALIGN=RIGHT><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$percentages[2]%</FONT></TD>
					<TD VALIGN=MIDDLE ALIGN=LEFT><TABLE CELLSPACING=0 CELLPADDING=0 CELLSPACING=0 BORDER=0><TR><TD><IMG SRC=http://www.godlessgeeks.com/IMAGES/blue_bar.GIF WIDTH=$sizes[2] HEIGHT=20></TD></TR></TABLE></TD>
        </TR>
<TR>          <TD VALIGN=top WIDTH=50% NOWRAP><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$in{s4} </FONT></TD>
          <TD VALIGN=MIDDLE NOWRAP ALIGN=RIGHT><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$percentages[3]%</FONT></TD>
					<TD VALIGN=MIDDLE ALIGN=LEFT><TABLE CELLSPACING=0 CELLPADDING=0 CELLSPACING=0 BORDER=0><TR><TD><IMG SRC=http://www.godlessgeeks.com/IMAGES/blue_bar.GIF WIDTH=$sizes[3] HEIGHT=20></TD></TR></TABLE></TD>
        </TR>

 
      </TABLE><BR>
      <CENTER>
<FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>Total Votes: $sum </FONT><BR>
<FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>$in{answer} </FONT><BR>
<BR>				
				
<BR>

<A HREF=http://godlessgeeks.com TARGET=""><FONT FACE=verdana,arial,sans-serif COLOR=000000 SIZE=2>Atheists of Silicon Valley</FONT></A>
      <BR>

<BR>
<!---- ADD FOR ATHEISTS OF SILICON VALLEY SERVICE --->
<TABLE WIDTH=100% BORDER=0 CELLSPACING=1 BGCOLOR=000000>
          <TR><TD align=center BGCOLOR=FFFFCC><TABLE WIDTH=100%><TR><TD><FONT FACE='verdana,arial,sans-serif'
	COLOR=000000 SIZE=1>Atheist Trivia is a free service sponsored by 
<a href=http://www.godlessgeeks.com> Atheists of Silicon Valley </a>
If you are an atheist, humanist, skeptic or similarly oriented organization and would like to use Atheist Trivia on your website, please contact 
<a href=mailto:stsam\@godlessgeeks.com>stsam\@godlessgeeks.com</a>
</TD>
<TD>

     <IMG SRC=http://www.godlessgeeks.com/map.jpg align=center border=0
		width=60 height=80>
</TD>
</TR>
</TABLE>
</CENTER>
    </TD>
  </TR>
</TABLE>


</BODY>
</HTML>
EOF

