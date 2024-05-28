package main

import (
	"encoding/json"
	"log"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
)

type Population struct {
	Location string  `json:"location"`
	Pop      float64 `json:"population"`
}

type HumanPresence struct {
	Location string  `json:"location"`
	Size     float64 `json:"human_presence_size"`
}

func main() {
	// Read population JSON
	var pop []Population
	err := json.Unmarshal([]byte(populationJSON), &pop)
	if err != nil {
		log.Fatal(err)
	}

	// Read human presence JSON
	var hp []HumanPresence
	err = json.Unmarshal([]byte(humanPresenceJSON), &hp)
	if err != nil {
		log.Fatal(err)
	}

	// Process data
	var locations []string
	var populations []float64
	var humanPresenceSizes []float64

	for _, p := range pop {
		locations = append(locations, p.Location)
		populations = append(populations, p.Pop)
	}

	for _, h := range hp {
		humanPresenceSizes = append(humanPresenceSizes, h.Size)
	}

	// Create 3D bar chart
	bar3D := charts.NewBar3D()
	bar3D.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "Population and Human Presence"}),
	)

	var data []opts.Chart3DData
	for i := range locations {
		data = append(data, opts.Chart3DData{Value: []interface{}{float64(i), populations[i], humanPresenceSizes[i]}})
	}

	bar3D.AddSeries("Population and Human Presence", data)

	// Save plot to file
	f, err := os.Create("population_human_presence.html")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	err = bar3D.Render(f)
	if err != nil {
		log.Fatal(err)
	}
}

const populationJSON = `
[
    {"location": "45.5152, -122.6784", "population": 1000},
    {"location": "45.5232, -122.6700", "population": 2000},
    {"location": "45.5352, -122.6600", "population": 3000}
]
`

const humanPresenceJSON = `
[
    {"location": "45.5152, -122.6784", "human_presence_size": 3},
    {"location": "45.5232, -122.6700", "human_presence_size": 40},
    {"location": "45.5352, -122.6600", "human_presence_size": 20}
]`
