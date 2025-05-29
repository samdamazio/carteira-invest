import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts";

const COLORS = [
  "#8884d8", "#82ca9d", "#ffc658", "#ff8042", "#a4de6c", "#d0ed57", "#8dd1e1", "#d88884"
];

const dataGeral = [
  { name: "Ações BR", value: 20 },
  { name: "ETFs Exterior", value: 20 },
  { name: "Renda Fixa (BR)", value: 20 },
  { name: "FIIs/REITs", value: 15 },
  { name: "Ações Exterior", value: 5 },
  { name: "Reserva de valor", value: 5 },
  { name: "Reserva de oportunidade", value: 5 }
];

const dataRendaFixa = [
  { name: "Tesouro IPCA+", value: 8 },
  { name: "Prefixado", value: 4 },
  { name: "CDB/LCI/LCA", value: 4 },
  { name: "Tesouro Selic", value: 4 }
];

const dataETFs = [
  { name: "Ações globais", value: 8 },
  { name: "Tech", value: 4 },
  { name: "Emergentes", value: 3 },
  { name: "Setores Saúde/Educação", value: 2 },
  { name: "Renda Fixa em dólar", value: 3 }
];

const dataFIIs = [
  { name: "FIIs Papel", value: 4.5 },
  { name: "FIIs Tijolo", value: 4.5 },
  { name: "FIIs Híbridos", value: 3 },
  { name: "REITs", value: 3 }
];

export default function CarteiraInterativa() {
  const [expandido, setExpandido] = useState("");

  const handleClick = (categoria) => {
    setExpandido(expandido === categoria ? "" : categoria);
  };

  const renderGrafico = (data, titulo) => (
    <div className="flex flex-col items-center">
      <h2 className="text-xl font-semibold mb-2">{titulo}</h2>
      <PieChart width={400} height={300}>
        <Pie
          data={data}
          cx={200}
          cy={150}
          outerRadius={100}
          fill="#8884d8"
          dataKey="value"
          onClick={(entry) => handleClick(entry.name)}
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>
    </div>
  );

  return (
    <div className="grid gap-4 p-4">
      <Card>
        <CardContent>
          {renderGrafico(dataGeral, "Composição Geral da Carteira")}
        </CardContent>
      </Card>

      {expandido === "Renda Fixa (BR)" && (
        <Card>
          <CardContent>{renderGrafico(dataRendaFixa, "Renda Fixa (BR)")}</CardContent>
        </Card>
      )}

      {expandido === "ETFs Exterior" && (
        <Card>
          <CardContent>{renderGrafico(dataETFs, "ETFs no Exterior")}</CardContent>
        </Card>
      )}

      {expandido === "FIIs/REITs" && (
        <Card>
          <CardContent>{renderGrafico(dataFIIs, "FIIs e REITs")}</CardContent>
        </Card>
      )}
    </div>
  );
}
