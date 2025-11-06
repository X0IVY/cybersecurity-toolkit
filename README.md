# 🔒 Cybersecurity Toolkit

A collection of network security tools I built while learning penetration testing and network analysis. Currently focused on reconnaissance and enumeration.

## Tools

### 1. Hash Generator (Python)
Generates cryptographic hashes for files and text strings. Useful for integrity checking and forensics.

**Supports:** MD5, SHA-1, SHA-256, SHA-512

```bash
python hash_tools.py
# Interactive menu:
# 1. Hash text
# 2. Hash file  
# 3. Exit
```

**Example output:**
```
Enter text: password123
MD5: 482c811da5d5b4bc6d497ffa98491e38
SHA-256: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

**Note:** MD5 and SHA-1 are cryptographically broken but included for legacy system compatibility.

### 2. Port Scanner (Go)
Fast concurrent TCP port scanner using goroutines. Scans ranges of ports to find open services.

```bash
go run port_scanner.go <host> <start_port> <end_port>

# Example:
go run port_scanner.go 192.168.1.1 1 1000
```

**Example output:**
```
Scanning 192.168.1.1 from port 1 to 1000...

[+] Port 22 is OPEN
[+] Port 80 is OPEN
[+] Port 443 is OPEN

Scan complete. Found 3 open ports in 2.3s
```

**Limitations:**
- 1 second timeout per port (can miss slow services)
- No service detection yet
- TCP only, no UDP support

## Installation

```bash
# Clone repo
git clone https://github.com/X0IVY/cybersecurity-toolkit.git
cd cybersecurity-toolkit

# Python dependencies
pip install -r requirements.txt

# Go (make sure Go is installed)
go version  # should be 1.16+
```

## Roadmap

- [ ] Add banner grabbing to port scanner
- [ ] Service version detection
- [ ] Export scan results to JSON/CSV
- [ ] Build simple vulnerable web app for testing
- [ ] Add subdomain enumeration tool

## Legal Disclaimer

**IMPORTANT:** These tools are for authorized security testing only.

- Only scan networks/systems you own or have explicit written permission to test
- Unauthorized port scanning is illegal in many jurisdictions
- I'm not responsible for misuse of these tools

If you're learning, set up your own lab environment (VirtualBox VMs, Docker containers, etc.)

## Learning Resources

While building this, I learned from:
- TryHackMe (network fundamentals)
- OWASP testing guides
- Go concurrency patterns documentation

## Known Issues

- Port scanner can trigger IDS/IPS systems (too fast/not stealthy)
- Hash tool doesn't handle very large files efficiently (loads entire file into memory)
- No progress indicator on long scans

## License

MIT License - see LICENSE file

## Contact

For questions or suggestions, open an issue.
