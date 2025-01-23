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

/**
 * Fetches results from the backend API based on a given prompt and active providers.
 * 
 * @param {string} prompt - The user's input to query the LLMs.
 * @param {Object} [activeProviders={}] - An object where keys are provider names and values are booleans indicating whether they are active.
 * @param {Object} [extraParams={}] - Additional query parameters such as `temperature` or `max_tokens`.
 * @returns {Promise<Object>} - A promise resolving to the API response data.
 * @throws {Error} - Throws an error if the API call fails.
 */
export const fetchResults = async (prompt, activeProviders ={}, extraParams = {}) => {
  try {
    //Extract active LLM providers and create the llm provider query param
    const activeProviderNames = Object.keys(activeProviders)
      .filter((provider) => activeProviders[provider]) // Include only active providers
      .join(",");

    //Merge all params
    const params = {
      llm_provider: activeProviderNames,
      ...extraParams
    }

    const response = await apiClient.post("/query", { prompt }, { params });
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

//HELPER FUNCTIONS
