/* eslint-env node */
/* global fetch */
const { GoogleGenAI } = require('@google/genai');
const dotenv = require('dotenv');

dotenv.config();

async function findModels() {
  const apiKey = process.env.VITE_GEMINI_API_KEY;
  if (!apiKey) {
    console.error('Error: VITE_GEMINI_API_KEY is not set in .env');
    return;
  }

  console.log('Fetching available Gemini models...');

  try {
    const ai = new GoogleGenAI({ apiKey });
    const response = await ai.models.list();
    const models = response.models || [];

    console.log(`Found ${models.length} total models.`);
    console.log('\nText/Generation models:');
    models.filter(m => m.name.includes('gemini') && !m.name.includes('vision') && !m.name.includes('embedding'))
          .forEach(m => console.log(`- ${m.name}`));

    console.log('\nVision/Multimodal models:');
    models.filter(m => m.name.includes('vision') || m.name.includes('pro'))
          .forEach(m => console.log(`- ${m.name}`));

  } catch (error) {
    console.error('Failed to fetch models:', error.message);
  }
}

findModels();
