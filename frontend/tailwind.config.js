/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Include all React components
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")], // Ensure DaisyUI is added as a plugin
  daisyui: {
    themes: [
      "light",
      "dark",
      "cyberpunk", // Ensure themes are included
    ],
  },
};
