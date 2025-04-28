=========================================
   Network Discovery Toolkit - README
   Version: 1.0
   Created: April 28, 2025
=========================================

This toolkit provides a simple way to scan a network to identify active IP addresses (live hosts) prior to conducting a vulnerability assessment or penetration test.

------------------------------------------------------------
TOOLS INCLUDED:
------------------------------------------------------------

1. Advanced IP Scanner (Portable - GUI)
   File: Advanced_IP_Scanner_Portable.exe
   Website: https://www.advanced-ip-scanner.com/

2. PowerShell Scripts (Command Line)
   - PingSweep.ps1
   - ExportLiveHosts.ps1

------------------------------------------------------------
📘 INSTRUCTIONS - ADVANCED IP SCANNER (RECOMMENDED FOR GUI)
------------------------------------------------------------

1. Launch `Advanced_IP_Scanner_Portable.exe`.
   - No installation needed.
   - You can run this directly on most Windows systems.

2. Enter the subnet to scan.
   - Example: 192.168.1.0 to 192.168.1.254

3. Click the green "Scan" button.

4. After scan completes:
   - Click `File > Save As...` to export results (CSV, TXT, XML)

5. Save your scan results in the `/Reports/` folder.

------------------------------------------------------------
📘 INSTRUCTIONS - POWERSHELL SCRIPT (CLI OPTION)
------------------------------------------------------------

PowerShell scripts are useful when a GUI is not available or for scripting automated scans.

HOW TO RUN:
1. Right-click the `.ps1` file and select `Run with PowerShell`
   - OR run via terminal: `.\PingSweep.ps1` or `.\ExportLiveHosts.ps1`

2. Enter the subnet prefix when prompted.
   - Example: `192.168.1.` (don’t forget the dot)

3. PingSweep.ps1:
   - Displays live hosts in real-time

4. ExportLiveHosts.ps1:
   - Saves live IPs to a text file in `/Reports/`
   - Filename includes timestamp for easy tracking

Note:
- These scripts use the built-in `Test-Connection` cmdlet.
- Results depend on ICMP (ping) responses. Devices with ICMP disabled will not show up.

------------------------------------------------------------
REPORTS
------------------------------------------------------------

Save all scan exports into the `Reports/` folder.
This helps track which tools were used and when.

------------------------------------------------------------
LEGAL & ETHICAL USAGE
------------------------------------------------------------

This toolkit is intended for use during **authorized** security assessments.
Always obtain written permission before scanning client or third-party networks.

------------------------------------------------------------

Created by: Burwood Group

Support Contact: cyber@burwood.com
