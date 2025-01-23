/* QueryDisplay
This component displays the current query and a list of active providers with distinct colors for each.
*/

import React from "react";

const QueryDisplay = ({ query, activeProviders }) => {
  return (
    <div className="p-4 border-b">
      <h2 className="font-bold text-lg mb-2">{query || "Your query will appear here"}</h2>
      <div className="flex space-x-2">
        {Object.entries(activeProviders).map(
          ([provider, isActive]) =>
            isActive && (
              <span
                key={provider}
                className={`px-2 py-1 rounded text-white ${
                  provider === "ChatGPT"
                    ? "bg-gray-400"
                : provider === "Gemini"
                    ? "bg-blue-500"
                : provider === "Claude"
                    ? "bg-orange-500"
                    : "bg-black"
                }`}
              >
                {provider}
              </span>
            )
        )}
      </div>
    </div>
  );
};

export default QueryDisplay;
