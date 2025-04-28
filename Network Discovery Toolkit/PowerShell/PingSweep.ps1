# Ping sweep to identify live hosts on a given subnet
$range = 1..254
$subnet = Read-Host "Enter subnet prefix (e.g., 192.168.1.)"
foreach ($i in $range) {
    $ip = "$subnet$i"
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
        Write-Host "$ip is alive"
    }
}