export const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve((reader.result as string).split(',')[1]);
        reader.onerror = error => reject(error);
    });
};

export const getLocalizedNumber = (num: number | string, lang: string = 'en'): string => {
    const localeMap: Record<string, string> = { hi: 'hi-IN', en: 'en-IN' };
    const locale = localeMap[lang] || 'en-IN';
    return Number(num).toLocaleString(locale);
};
