<html><title>PHP test</title><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<body><h1>PHP test</h1>
<?php
$var=1;
$str="Bob";
echo "<p>Hello world<br>";
echo $str, " ", $var, "<p>";
$str2="I have $var uncle named $str<p>";
echo $str2;
echo "I have only $var uncle named $str<p>";
$today = date("Y/m/d");
$str3 = $today." is today's date<br>";
echo $str3;
echo $today." is today's date, again<br>";
 ?>
</body></html>