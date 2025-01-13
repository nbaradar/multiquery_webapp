import React from "react";

const ResultCard = ({ result }) => {
  return (
    <div
      className={`p-4 border rounded shadow ${
        result.color === "red"
          ? "border-red-500"
          : result.color === "blue"
          ? "border-blue-500"
          : "border-orange-500"
      }`}
    >
      <h3
        className={`font-bold ${
          result.color === "red"
            ? "text-red-500"
            : result.color === "blue"
            ? "text-blue-500"
            : "text-orange-500"
        }`}
      >
        {result.provider}
      </h3>
      <p>{result.response}</p>
    </div>
  );
};

export default ResultCard;
