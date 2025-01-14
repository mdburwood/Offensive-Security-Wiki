# Reconnaissance

## Overview
Reconnaissance is the first and foundational phase in the penetration testing (pentesting) process. It involves gathering as much information as possible about the target to identify potential attack vectors. This phase can be divided into two types:

1. **Passive Reconnaissance**: Collecting information without directly interacting with the target system.
2. **Active Reconnaissance**: Involves direct interaction with the target system to gather data.

A thorough reconnaissance process enables pentesters to tailor their approach, maximizing the chances of identifying vulnerabilities.

---

## Tools for Reconnaissance

### 1. **Passive Reconnaissance Tools**
#### A. OSINT (Open Source Intelligence) Tools
1. Paid
- **[Maltego](https://www.maltego.com/)**: Social media, personal discovery mechnaism
- **[Shodan](https://www.shodan.io/)**: Discover internet-connected devices and services with detailed metadata.
2. Open Source
- **[theHarvester](https://github.com/laramies/theHarvester)**: Gather emails, subdomains, IPs, and other metadata. Requires API-keys to be effective
- **[Amass](https://github.com/owasp-amass/amass)**: Map subdomains and domains using OSINT and DNS enumeration.

#### B. Search Engines and Databases
- **Google Dorking**: Advanced search operators to uncover sensitive information.
- **Censys**: Another device search engine for internet-connected systems.
- **Have I Been Pwned**: Check if credentials have been leaked in breaches.

### 2. **Active Reconnaissance Tools**
#### A. DNS and Network Mapping
- **Nmap**: Network scanning and port enumeration.
- **Masscan**: High-speed port scanner for large IP ranges.
- **Fierce**: DNS reconnaissance tool for identifying subdomains.

#### B. Web Application Recon
- **Burp Suite**: Proxy-based web application testing.
- **Nikto**: Scans web servers for vulnerabilities and misconfigurations.
- **Gobuster**: Directory and DNS brute-forcing.

#### C. Email and User Enumeration
- **Email2Phonenumber**: Derive phone numbers from email addresses.
- **Hunter.io**: Find corporate email formats and employee details.

#### D. Vulnerability Scanning
- **OpenVAS**: Comprehensive vulnerability scanning.
- **Nessus**: Commercial vulnerability scanner for network and application assessments.

### 3. **Social Engineering Recon Tools**
- **SET (Social Engineer Toolkit)**: Framework for social engineering attacks.
- **SpiderFoot**: Automated OSINT gathering with social engineering insights.

---

## Key Steps in Reconnaissance

### 1. **Identify the Scope**
   - Define the target assets (domains, IP ranges, web applications).
   - Understand engagement rules (e.g., passive only).

### 2. **Information Collection**
   - Gather domain registrant data using WHOIS.
   - Extract subdomains and DNS records.
   - Identify exposed services and ports.

### 3. **Analyze Data**
   - Cross-reference data from multiple tools.
   - Prioritize targets based on exposed vulnerabilities and services.

### 4. **Document Findings**
   - Log all gathered information for reporting and analysis.
   - Ensure compliance with the defined scope and rules of engagement.

---

## Best Practices

1. Use passive reconnaissance first to avoid detection.
2. Respect the engagement's legal and ethical boundaries.
3. Validate findings with multiple tools to reduce false positives.
4. Maintain a detailed record of tools and commands for reproducibility.
5. Prioritize stealth during active reconnaissance to minimize detection risk.

---

## Additional Resources
- [OWASP Testing Guide](https://owasp.org/)
- [Kali Linux Tools](https://www.kali.org/tools/)
- [Recon-ng Documentation](https://github.com/lanmaster53/recon-ng/wiki)

By following the steps outlined above and leveraging the recommended tools, pentesters can perform thorough reconnaissance to support successful engagements.

