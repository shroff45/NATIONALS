/* eslint-env node */

require('dotenv').config();

const apiKey = process.env.VITE_GEMINI_API_KEY;

if (!apiKey) {
    console.error("VITE_GEMINI_API_KEY is missing from environment variables.");
    process.exit(1);
}

const url = `https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`;

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log("Available Models:");
        if (data.models) {
            data.models.forEach(model => {
                console.log(`- ${model.name}`);
                console.log(`  Description: ${model.description}`);
                console.log(`  Supported Generation Methods: ${model.supportedGenerationMethods.join(', ')}`);
                console.log('---');
            });
        } else {
            console.log("Unexpected response format:", data);
        }
    })
    .catch(error => {
        console.error("Error fetching models:", error);
    });
