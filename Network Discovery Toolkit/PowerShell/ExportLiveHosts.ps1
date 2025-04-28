$range = 1..254
$subnet = Read-Host "Enter subnet prefix (e.g., 192.168.1.)"
$liveHosts = @()
foreach ($i in $range) {
    $ip = "$subnet$i"
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
        $liveHosts += $ip
    }
}
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$filename = ".\Reports\live_hosts_$timestamp.txt"
$liveHosts | Out-File -FilePath $filename
Write-Host "Results saved to $filename"