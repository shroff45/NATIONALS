export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            const base64String = reader.result as string;
            // The Gemini API usually expects the base64 data without the data URL prefix
            const base64Data = base64String.split(',')[1];
            resolve(base64Data);
        };
        reader.onerror = (error) => reject(error);
    });
};

export const getLocalizedNumber = (num: number | string, language: string = 'en'): string => {
    try {
        const numberToFormat = typeof num === 'string' ? parseFloat(num) : num;
        if (isNaN(numberToFormat)) return String(num);
        return new Intl.NumberFormat(language === 'hi' ? 'hi-IN' : 'en-IN').format(numberToFormat);
    } catch (e) {
        return String(num);
    }
};
