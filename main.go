package main
import (
    "fmt"
    "time"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "System Operational: %s", time.Now())
    })
    log.Println("Starting high-performance service on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
