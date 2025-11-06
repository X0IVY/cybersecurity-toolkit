# Changelog

## [Nov 6, 2025]

### Added
- Banner grabbing to port scanner
- Service detection for 15 common ports (SSH, HTTP, MySQL, etc.)
- Better output showing service names alongside ports

### Changed
- Increased banner grab timeout to 2s (was getting false negatives)
- Port scanner now shows "[*] Banner grabbing enabled" message

### Notes
- Banner grabbing makes scans slower but way more useful
- HTTP servers respond well but some services timeout
- Need to add better error handling for banner grabs

---

## [Earlier today]

### Changed
- Updated README to only show tools that actually exist
- Removed fake feature list (Password Analyzer, Traffic Monitor, etc.)
- Added real usage examples with command output
- Added limitations section - being honest about what doesn't work

### Notes
- README was way too optimistic before
- Better to show what's real than promise stuff that doesn't exist

---

## [Start of project]

### Added
- Hash generator tool (MD5, SHA-1, SHA-256, SHA-512)
- Basic port scanner using Go goroutines
- Colorama for terminal colors
- MIT license

### Notes
- Started with Python hash tool, seemed like easiest security tool to build
- Wanted to learn Go so built port scanner in that
- MD5/SHA-1 are broken but kept them for legacy stuff

### Issues found
- Hash tool loads entire file into memory (bad for big files)
- Port scanner timeout of 1s can miss slow services
- No progress bar on long scans
