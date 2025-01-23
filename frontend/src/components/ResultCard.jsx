import React from "react";

const ResultCard = ({ result }) => {
  return (
    <div className={`p-4 border rounded shadow ${result.bg_color}`}>
      <h3 className={`font-bold ${result.text_color }`}>
        {result.provider}
      </h3>
      <p>{result.response}</p>
    </div>
  );
};

export default ResultCard;
