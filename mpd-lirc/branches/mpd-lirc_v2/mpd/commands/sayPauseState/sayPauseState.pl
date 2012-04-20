#!/usr/bin/perl
use strict;
use constant RANDOM_ON => "random\: on";
use constant RANDOM_OFF => "random\: off";

my $random_state = '';
my $app_state = `mpc | tail -n1`;

if($app_state =~ m/random\:\s\w*/) {
	$random_state = $&;
}

print "Random state: ".$random_state."\n";

if($random_state eq "random: on") {
	print "Random is on \n";
	`aplay $ENV{'MPD_LIRC_ROOT'}/sounds/voice/random_is_on.wav`
} else {
	print "Random is off \n";
	`aplay $ENV{'MPD_LIRC_ROOT'}/sounds/voice/random_is_off.wav`
}
