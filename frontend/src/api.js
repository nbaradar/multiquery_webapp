/*
Contains logic for all the API calls you'll make to the different subsystems of ContextCore.
*/

import axios from "axios";

// Create an axios client instance
const MULTIQUERY_API_URL = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";
const apiClient = axios.create({
  baseURL: MULTIQUERY_API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Function to fetch results
export const fetchResults = async (prompt) => {
  try {
    const response = await apiClient.post("/query", { prompt });
    return response.data; // Axios automatically parses JSON
  } catch (error) {
    // Extract error message for better debugging
    if (error.response) {
      // Server responded with a status outside the 2xx range
      throw new Error(`API Error: ${error.response.status} - ${error.response.data.detail || error.response.statusText}`);
    } else if (error.request) {
      // No response received
      throw new Error("No response received from the server. Please check your network connection.");
    } else {
      // Something else happened while setting up the request
      throw new Error(`Unexpected Error: ${error.message}`);
    }
  }
};
