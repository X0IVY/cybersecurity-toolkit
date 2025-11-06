package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

// tried to grab service banner
func grabBanner(host string, port int) string {
	addr := fmt.Sprintf("%s:%d", host, port)
	conn, err := net.DialTimeout("tcp", addr, 2*time.Second)
	if err != nil {
		return ""
	}
	defer conn.Close()

	// set read deadline
	conn.SetReadDeadline(time.Now().Add(2 * time.Second))
	
	// try sending HTTP request for web servers
	if port == 80 || port == 8080 || port == 8000 {
		fmt.Fprintf(conn, "GET / HTTP/1.0\r\n\r\n")
	}

	// read response
	reader := bufio.NewReader(conn)
	banner, err := reader.ReadString('\n')
	if err != nil {
		return ""
	}
	
	return strings.TrimSpace(banner)
}

// guess service based on port
func guessService(port int) string {
	services := map[int]string{
		21:   "FTP",
		22:   "SSH",
		23:   "Telnet",
		25:   "SMTP",
		53:   "DNS",
		80:   "HTTP",
		110:  "POP3",
		143:  "IMAP",
		443:  "HTTPS",
		445:  "SMB",
		3306: "MySQL",
		3389: "RDP",
		5432: "PostgreSQL",
		5900: "VNC",
		8080: "HTTP-Alt",
	}
	
	if service, ok := services[port]; ok {
		return service
	}
	return "Unknown"
}

func scanPort(host string, port int, wg *sync.WaitGroup, results chan<- string) {
	defer wg.Done()
	addr := fmt.Sprintf("%s:%d", host, port)
	conn, err := net.DialTimeout("tcp", addr, 1*time.Second)
	
	if err == nil {
		conn.Close()
		
		// get service name
		service := guessService(port)
		
		// try banner grab
		banner := grabBanner(host, port)
		
		result := fmt.Sprintf("[+] Port %d is OPEN (%s)", port, service)
		if banner != "" {
			// trim banner if too long
			if len(banner) > 60 {
				banner = banner[:60] + "..."
			}
			result += fmt.Sprintf(" - %s", banner)
		}
		
		results <- result
	}
}

func main() {
	if len(os.Args) < 4 {
		fmt.Println("usage: go run port_scanner.go <host> <start_port> <end_port>")
		fmt.Println("example: go run port_scanner.go 192.168.1.1 1 1000")
		os.Exit(1)
	}

	host := os.Args[1]
	startPort, _ := strconv.Atoi(os.Args[2])
	endPort, _ := strconv.Atoi(os.Args[3])

	if startPort > endPort || startPort < 1 || endPort > 65535 {
		fmt.Println("invalid port range")
		os.Exit(1)
	}

	fmt.Printf("\nScanning %s from port %d to %d...\n", host, startPort, endPort)
	fmt.Println("[*] Banner grabbing enabled\n")
	start := time.Now()

	var wg sync.WaitGroup
	results := make(chan string, 100)

	// launch goroutines
	for port := startPort; port <= endPort; port++ {
		wg.Add(1)
		go scanPort(host, port, &wg, results)
	}

	// close results when done
	go func() {
		wg.Wait()
		close(results)
	}()

	openPorts := 0
	for result := range results {
		fmt.Println(result)
		openPorts++
	}

	elapsed := time.Since(start)
	fmt.Printf("\nScan complete. Found %d open ports in %s\n", openPorts, elapsed)
}
