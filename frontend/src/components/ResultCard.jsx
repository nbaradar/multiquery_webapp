import React from "react";
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import rehypeRaw from "rehype-raw"

const ResultCard = ({ result }) => {
  return (
    <div className={`p-4 border rounded shadow ${result.bg_color}`}>
      <h3 className={`font-bold ${result.text_color }`}>
        {result.provider}
      </h3>
      {/* Render the response as Markdown */}
      <ReactMarkdown
        children={result.response}
        remarkPlugins={[remarkGfm]} // Enables GitHub-Flavored Markdown
        rehypePlugins={[rehypeRaw]} // Allows rendering raw HTML (use cautiously)
        className="prose" // Tailwind class for better typography (optional)
      />
    </div>
  );
};

export default ResultCard;
