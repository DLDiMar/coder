const morseCodeMapping = {
    A: ".-",
    B: "-...",
    C: "-.-.",
    D: "-..",
    E: ".",
    F: "..-.",
    G: "--.",
    H: "....",
    I: "..",
    J: ".---",
    K: "-.-",
    L: ".-..",
    M: "--",
    N: "-.",
    O: "---",
    P: ".--.",
    Q: "--.-",
    R: ".-.",
    S: "...",
    T: "-",
    U: "..-",
    V: "...-",
    W: ".--",
    X: "-..-",
    Y: "-.--",
    Z: "--..",
    " ": "^",
  };
  
  function toMorse(message) {
    return message
      .split("")
      .map(char => {
        return char.toUpperCase().trim() === " " ? "^" : morseCodeMapping[char.toUpperCase()];
      })
      .join(" ");
  }
  
  const input = "Hello Bob";
  const output = toMorse(input);
  console.log("Input:", input);
  console.log("Output:", output);

  console.log(113 % 11)
  console.log(4%2)