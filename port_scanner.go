package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"sync"
	"time"
)

// quick scan function, tries to connect to a port
func scanPort(host string, port int, wg *sync.WaitGroup, results chan<- string) {
	defer wg.Done()
	addr := fmt.Sprintf("%s:%d", host, port)
	conn, err := net.DialTimeout("tcp", addr, 1*time.Second)
	
	if err == nil {
		results <- fmt.Sprintf("[+] Port %d is OPEN", port)
		conn.Close()
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

	fmt.Printf("\nScanning %s from port %d to %d...\n\n", host, startPort, endPort)
	start := time.Now()

	var wg sync.WaitGroup
	results := make(chan string, 100)

	// launch goroutines for each port
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
