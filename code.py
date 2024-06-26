# Define the simulator
set ns [new Simulator]

# Open the NAM trace file
set nf [open ddos_attack.nam w]
$ns namtrace-all $nf

# Define a finish procedure
proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    exec nam ddos_attack.nam &
    exit 0
}

# Create nodes
set victim [$ns node]
set router1 [$ns node]
set router2 [$ns node]

# Create attacking nodes
set attackers {}
for {set i 0} {$i < 5} {incr i} {
    set attacker [$ns node]
    lappend attackers $attacker
    $ns duplex-link $attacker $router1 1Mb 10ms DropTail
}

# Create links
$ns duplex-link $router1 $router2 10Mb 10ms DropTail
$ns duplex-link $router2 $victim 1Mb 10ms DropTail

# Set up traffic from attackers to victim
foreach attacker $attackers {
    set udp [new Agent/UDP]
    $ns attach-agent $attacker $udp

    set null [new Agent/Null]
    $ns attach-agent $victim $null

    $ns connect $udp $null

    set cbr [new Application/Traffic/CBR]
    $cbr set packetSize_ 1000
    $cbr set interval_ 0.01
    $cbr attach-agent $udp
    $ns at 1.0 "$cbr start"
}

# Schedule the finish procedure
$ns at 10.0 "finish"

# Run the simulation
$ns run
