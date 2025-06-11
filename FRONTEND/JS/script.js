let transactions = [];
let budgetLimit = 1000;

function addTransaction() {
  const description = document.getElementById("description").value;
  const amount = parseFloat(document.getElementById("amount").value);
  const category = document.getElementById("category").value;
  const type = document.getElementById("type").value;

  if (!description || !amount || !category) return;

  transactions.push({ description, amount, category, type });
  updateSummary();
  updateChart();
}

function updateSummary() {
  const receitas = transactions.filter(t => t.type === 'receita').reduce((acc, t) => acc + t.amount, 0);
  const despesas = transactions.filter(t => t.type === 'despesa').reduce((acc, t) => acc + t.amount, 0);
  const saldo = receitas - despesas;
  const progresso = (despesas / budgetLimit) * 100;

  document.getElementById("receitas").textContent = `Receitas: R$ ${receitas.toFixed(2)}`;
  document.getElementById("despesas").textContent = `Despesas: R$ ${despesas.toFixed(2)}`;
  document.getElementById("saldo").textContent = `Saldo: R$ ${saldo.toFixed(2)}`;

  let sugestao = "";
  if (saldo < 0) sugestao = "Você está gastando mais do que ganha. Considere reduzir despesas.";
  else if (saldo > 0 && progresso < 50) sugestao = "Parabéns! Você está dentro do seu orçamento.";
  else if (progresso >= 100) sugestao = "Atenção! Você ultrapassou seu limite de orçamento.";
  else sugestao = "Continue acompanhando suas finanças para manter o equilíbrio.";

  document.getElementById("sugestao").textContent = sugestao;
}

let chart;
function updateChart() {
  const receitas = transactions.filter(t => t.type === 'receita').reduce((acc, t) => acc + t.amount, 0);
  const despesas = transactions.filter(t => t.type === 'despesa').reduce((acc, t) => acc + t.amount, 0);

  const ctx = document.getElementById("grafico").getContext("2d");
  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Receitas', 'Despesas'],
      datasets: [{
        label: 'Finanças',
        data: [receitas, despesas],
        backgroundColor: ['#4CAF50', '#F44336']
      }]
    }
  });
}
