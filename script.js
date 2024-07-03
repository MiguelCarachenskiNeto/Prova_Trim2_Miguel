var meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Septembro", "Outubro", "Novembro", "Dezembro"];

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question("\nDigite um mês em números (1-12): ", data => {
  console.log("")
  for (var i = 0; i < data; i++) {
    console.log ("- ", meses[i]);
  }
  console.log("\nNasci em " + meses[data-1]);
  process.exit
});



