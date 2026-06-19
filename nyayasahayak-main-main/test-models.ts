import { GoogleGenAI } from '@google/genai';

async function testModels() {
  console.log('Testing available models...');

  try {
    const ai = new GoogleGenAI({ apiKey: process.env.VITE_GEMINI_API_KEY });

    // Test list_models
    console.log('\nFetching models...');
    const response = await ai.models.list();
    console.log('Models found:', response.models?.length);

    // Find gemini models
    const geminiModels = response.models?.filter(m => m.name.includes('gemini'));
    console.log('\nGemini models available:');
    geminiModels?.forEach(m => console.log(`- ${m.name} (${m.description})`));

  } catch (error) {
    console.error('Error:', error);
  }
}

// @ts-ignore
testModels();
