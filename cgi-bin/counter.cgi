

#!/usr/bin/perl

open(FILE,"<count.txt");
$count = <FILE>;
close(FILE);

$count++;

open(FILE,">count.txt");
print FILE $count;
close(FILE);

print "Content-type:text/html\n\n";
print $count;
