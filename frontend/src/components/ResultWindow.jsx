import React from "react";
import ResultCard from "./ResultCard";

const ResultsWindow = ({ results }) => {
  return (
    <div className="flex-grow p-4 overflow-y-auto grid grid-cols-1 gap-4">
      {results.map((result, index) => (
        <ResultCard key={index} result={result} />
      ))}
    </div>
  );
};

export default ResultsWindow;
