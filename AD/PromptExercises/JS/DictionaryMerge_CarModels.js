const readline = require('readline');

function pauseConsole() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Press Enter to exit...', () => {
        rl.close();
    });
}

function updateInventory(carsAvailable, inventory) {
    const updatedInventory = {};
    try {
        Object.entries(carsAvailable).forEach(([make, available]) => {
            if (available === "True") {
                updatedInventory[make] = {};
                const inventoryForMake = inventory[make];
                if (inventoryForMake) {
                    Object.entries(inventoryForMake).forEach(([model, data]) => {
                        const regex = new RegExp(`(?<=\\b${make}\\b).*$`);
                        if (regex.test(model)) {
                            updatedInventory[make][model] = data;
                        } else {
                            throw new Error(`Invalid model name for make ${make}: ${model}`);
                        }
                    });
                }
            }
        });
    } catch (error) {
        console.error(error);
    }
    return updatedInventory;
}

let carsAvailable = 
{
  "Ford": "True",
  "Toyota": "True",
  "Honda": "True",
  "Hyundai": "False"
}

let inventoryFord = 
{
  "1": "1997 Tauros",
  "2": "2001 Explorer",
}

let inventoryToyota =
{
  "1": "2007 Corrola"
}

let k = updateInventory(carsAvailable, {
    Ford: inventoryFord,
    Toyota: inventoryToyota
});
console.log("The merged values: " + k);
pauseConsole();